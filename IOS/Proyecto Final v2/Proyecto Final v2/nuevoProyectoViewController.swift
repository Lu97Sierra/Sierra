//
//  nuevoProyectoViewController.swift
//  Proyecto Final v2
//
//  Created by Gustavo on 06/12/23.
//  Copyright © 2023 Gustavo. All rights reserved.
//

import Foundation
import UIKit
import CoreData

class nuevoProyectoViewController: UIViewController {

    // Conecta tus IBOutlets aquí
    @IBOutlet weak var nombreProyectoTextField: UITextField!
    @IBOutlet weak var descripcionProyectoTextField: UITextField!
    @IBOutlet weak var fechaLimiteDatePicker: UIDatePicker!

    // Otras propiedades y métodos

    @IBAction func guardarTapped(_ sender: Any) {
        // Crear referencia al contexto de Core Data
        let context = (UIApplication.shared.delegate as! AppDelegate).persistentContainer.viewContext
        
        // Crear una nueva instancia de la entidad Proyecto
        let nuevoProyecto = Proyectos(context: context)
        
        // Configurar los atributos del nuevo proyecto
        nuevoProyecto.nombreProyecto = nombreProyectoTextField.text
        nuevoProyecto.descripcion = descripcionProyectoTextField.text
        nuevoProyecto.fecha_limite = fechaLimiteDatePicker.date
        
        // Intentar guardar el nuevo proyecto
        do {
            try context.save()
            // Limpiar los campos después de guardar
            limpiarCampos()
            // Mostrar mensaje de éxito
            mostrarAlertaDeExito()
        } catch {
            // Si hay un error, mostrar un mensaje de error
            mostrarAlerta(mensaje: "Hubo un error al guardar el proyecto.")
        }
    }

    // Función para mostrar una alerta genérica
    func mostrarAlerta(mensaje: String, titulo: String = "Error") {
        let alerta = UIAlertController(title: titulo, message: mensaje, preferredStyle: .alert)
        alerta.addAction(UIAlertAction(title: "OK", style: .default))
        present(alerta, animated: true)
    }
    func limpiarCampos() {
        nombreProyectoTextField.text = ""
        descripcionProyectoTextField.text = ""
        fechaLimiteDatePicker.date = Date() 
    }

    // Función para mostrar una alerta de éxito y luego volver a la pantalla anterior
    func mostrarAlertaDeExito() {
        let alerta = UIAlertController(title: "Éxito", message: "El proyecto se guardó correctamente", preferredStyle: .alert)
        alerta.addAction(UIAlertAction(title: "OK", style: .default, handler: { [weak self] _ in
            // Encontrar el UITabBarController
            if let tabBarController = self?.navigationController?.viewControllers.first(where: { $0 is UITabBarController }) as? UITabBarController {
                // Seleccionar el índice del tab de listado
                tabBarController.selectedIndex = 0 // Cambia el 0 por el índice correcto de tu pestaña de listado

                // Navegar al UITabBarController
                self?.navigationController?.popToViewController(tabBarController, animated: true)
            }
        }))
        present(alerta, animated: true, completion: nil)
    }


}
