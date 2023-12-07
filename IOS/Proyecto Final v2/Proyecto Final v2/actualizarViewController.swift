//
//  actualizarViewController.swift
//  Proyecto Final v2
//
//  Created by Gustavo on 06/12/23.
//  Copyright © 2023 Gustavo. All rights reserved.
//

import Foundation
import UIKit
import CoreData

class actualizarViewController: UIViewController {
    // IBOutlets para tus campos de texto y date picker
    @IBOutlet weak var nombreProyectoTextField: UITextField!
    @IBOutlet weak var descripcionTextField: UITextField!
    @IBOutlet weak var fechaLimiteDatePicker: UIDatePicker!
    
    
    var proyecto: Proyectos?

    override func viewDidLoad() {
        super.viewDidLoad()
        // Configura los campos con los datos de 'proyecto'
        if let proyectoDetalle = proyecto {
            nombreProyectoTextField.text = proyectoDetalle.nombreProyecto
            descripcionTextField.text = proyectoDetalle.descripcion
            fechaLimiteDatePicker.date = proyectoDetalle.fecha_limite ?? Date()
        }
    }
    
    // Resto del código...
    @IBAction func guardarCambiosTapped(_ sender: Any) {
        if let proyectoDetalle = proyecto,
           let appDelegate = UIApplication.shared.delegate as? AppDelegate {
            let context = appDelegate.persistentContainer.viewContext
            proyectoDetalle.nombreProyecto = nombreProyectoTextField.text
            proyectoDetalle.descripcion = descripcionTextField.text
            proyectoDetalle.fecha_limite = fechaLimiteDatePicker.date
            
            do {
                try context.save()
                mostrarAlertaDeExito()
            } catch {
                mostrarAlerta(mensaje: "Hubo un error al guardar los cambios.")
            }
        }
    }
    func mostrarAlertaDeExito() {
        let alerta = UIAlertController(title: "Éxito", message: "El proyecto se actualizó correctamente", preferredStyle: .alert)
        alerta.addAction(UIAlertAction(title: "OK", style: .default, handler: { [weak self] _ in
            self?.navigationController?.popViewController(animated: true)
        }))
        present(alerta, animated: true, completion: nil)
    }
    func mostrarAlerta(mensaje: String) {
        let alert = UIAlertController(title: "Error", message: mensaje, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        self.present(alert, animated: true, completion: nil)
    }


}
