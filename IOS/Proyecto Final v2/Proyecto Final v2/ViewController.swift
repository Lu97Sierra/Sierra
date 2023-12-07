//
//  ViewController.swift
//  Proyecto Final v2
//
//  Created by Gustavo on 05/12/23.
//  Copyright © 2023 Gustavo. All rights reserved.
//

import UIKit
import CoreData

class ViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var usuarioTextField: UITextField!
    @IBOutlet weak var contraseñaTextField: UITextField!
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        usuarioTextField.delegate = self
    }
    

    @IBAction func IniciarSesion(_ sender: Any) {
        if usuarioTextField.text?.isEmpty ?? true || contraseñaTextField.text?.isEmpty ?? true {
                // Mostrar alerta diciendo que ambos campos son requeridos
                mostrarAlerta(mensaje: "Por favor, ingresa tanto el nombre de usuario como la contraseña.")
            } else {
                    // Realizar la lógica de inicio de sesión aquí
                guard let appDelegate = UIApplication.shared.delegate as? AppDelegate else {
                    return
                }
                let context = appDelegate.persistentContainer.viewContext

                let request = NSFetchRequest<NSFetchRequestResult>(entityName: "Perfilesdatos")
                request.predicate = NSPredicate(format: "usuario = %@ AND contrasena = %@", usuarioTextField.text!, contraseñaTextField.text!)

                do {
                    let result = try context.fetch(request)
                    if result.count > 0 {
                        //self.performSegue(withIdentifier: "inicioSesionExitoso", sender: self)

                    } else {
                        // Mostrar alerta de que las credenciales son incorrectas
                        mostrarAlertaDeCredencialesIncorrectas()
                    }
                } catch {
                    print("Error al realizar la solicitud: \(error)")
                }

            }

    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        if textField == usuarioTextField {
            cargarImagenDelUsuario()
            contraseñaTextField.becomeFirstResponder()
        }
        return true
    }

    
    func textFieldDidEndEditing(_ textField: UITextField) {
        if textField == usuarioTextField {
            cargarImagenDelUsuario()
        }
    }

    func cargarImagenDelUsuario() {
        guard let nombreUsuario = usuarioTextField.text, !nombreUsuario.isEmpty else {
            imageView.image = UIImage(systemName: "person.fill") // Imagen por defecto si el campo está vacío
            return
        }
        
        let appDelegate = UIApplication.shared.delegate as! AppDelegate
        let context = appDelegate.persistentContainer.viewContext
        let fetchRequest: NSFetchRequest<Perfilesdatos> = Perfilesdatos.fetchRequest()
        fetchRequest.predicate = NSPredicate(format: "usuario = %@", nombreUsuario)
        
        do {
            let resultados = try context.fetch(fetchRequest)
            if let perfil = resultados.first, let imagenData = perfil.imagen_logo as Data? {
                imageView.image = UIImage(data: imagenData)
            } else {
                imageView.image = UIImage(systemName: "person.fill") // Imagen por defecto si no se encuentra la imagen
            }
        } catch {
            print("Error al recuperar la imagen: \(error)")
        }
    }

    func mostrarAlertaDeCredencialesIncorrectas() {
        let alerta = UIAlertController(title: "Credenciales Incorrectas", message: "El nombre de usuario o la contraseña que has introducido son incorrectos. Por favor, inténtalo de nuevo.", preferredStyle: .alert)
        alerta.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        self.present(alerta, animated: true, completion: nil)
    }
    
    func mostrarAlerta(mensaje: String) {
        let alert = UIAlertController(title: "Error", message: mensaje, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        self.present(alert, animated: true, completion: nil)
    }

}



