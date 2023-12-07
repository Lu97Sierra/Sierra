//
//  RegistroViewController.swift
//  Proyecto Final v2
//
//  Created by Gustavo on 05/12/23.
//  Copyright © 2023 Gustavo. All rights reserved.
//

import Foundation
import UIKit    
import CoreData

class RegistroViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {

    // Conecta tus IBOutlets aquí, por ejemplo:
    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var nombreTextField: UITextField!
    @IBOutlet weak var correoTextField: UITextField!
    @IBOutlet weak var contraseñaTextField: UITextField!
    @IBOutlet weak var confirmarContraseñaTextField: UITextField!
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Otras configuraciones iniciales si las hay
    }

    @IBAction func seleccionarImagenTapped(_ sender: Any) {
        let imagePickerController = UIImagePickerController()
        imagePickerController.delegate = self
        imagePickerController.sourceType = .photoLibrary
        present(imagePickerController, animated: true, completion: nil)
    }
    
    // UIImagePickerControllerDelegate Methods
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        if let selectedImage = info[.originalImage] as? UIImage {
            imageView.image = selectedImage
        }
        picker.dismiss(animated: true, completion: nil)
    }

    @IBAction func registrarTapped(_ sender: Any) {
        guard let nombre = nombreTextField.text, !nombre.isEmpty,
              let correo = correoTextField.text, !correo.isEmpty,
              let contraseña = contraseñaTextField.text, contraseña == confirmarContraseñaTextField.text,
              let imageData = imageView.image?.jpegData(compressionQuality: 0.75) else {
            // Mostrar alerta de error si la validación falla
            mostrarAlerta(mensaje: "Por favor, asegúrate de que todos los campos estén llenos y las contraseñas coincidan.")
            return
        }
        
        // Aquí guardas los datos en Core Data
        let appDelegate = UIApplication.shared.delegate as! AppDelegate
        let context = appDelegate.persistentContainer.viewContext
        let nuevoUsuario = NSEntityDescription.insertNewObject(forEntityName: "Perfilesdatos", into: context)
        nuevoUsuario.setValue(nombre, forKey: "usuario")
        nuevoUsuario.setValue(correo, forKey: "correo")
        nuevoUsuario.setValue(contraseña, forKey: "contrasena")
        nuevoUsuario.setValue(imageData, forKey: "imagen_logo")
        
        do {
            try context.save()
            // Volver a la pantalla de inicio de sesión o mostrar confirmación aquí
            mostrarAlertaDeExito()
        } catch {
            mostrarAlerta(mensaje: "Hubo un error al guardar la información del usuario.")
        }
    }
    
    func mostrarAlertaDeExito() {
        let alerta = UIAlertController(title: "Éxito", message: "Registro completado con éxito.", preferredStyle: .alert)
        
        alerta.addAction(UIAlertAction(title: "OK", style: .default, handler: { [weak self] _ in
            // Dismiss your view controller to go back
            self?.navigationController?.popViewController(animated: true)
        }))
        
        present(alerta, animated: true, completion: nil)
    }
    
    
    func mostrarAlerta(mensaje: String) {
        let alerta = UIAlertController(title: "Error", message: mensaje, preferredStyle: .alert)
        alerta.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        present(alerta, animated: true, completion: nil)
    }
}





