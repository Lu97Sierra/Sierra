//
//  listadoViewController.swift
//  Proyecto Final v2
//
//  Created by Gustavo on 06/12/23.
//  Copyright © 2023 Gustavo. All rights reserved.
//

import UIKit
import CoreData

class listadoViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    
    @IBOutlet weak var tableView: UITableView!
    
    var proyectos: [Proyectos] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.dataSource = self
        tableView.delegate = self
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        cargarProyectos()
        tableView.reloadData()
    }

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        if let detalleVC = storyboard?.instantiateViewController(withIdentifier: "updateViewController") as? actualizarViewController {
            detalleVC.proyecto = proyectos[indexPath.row]
            navigationController?.pushViewController(detalleVC, animated: true)
        }
    }
    
    func cargarProyectos() {
        let appDelegate = UIApplication.shared.delegate as! AppDelegate
        let context = appDelegate.persistentContainer.viewContext
        let fetchRequest: NSFetchRequest<Proyectos> = Proyectos.fetchRequest()
        
        do {
            proyectos = try context.fetch(fetchRequest)
        } catch let error as NSError {
            print("No se pudo recuperar los datos: \(error), \(error.userInfo)")
        }
    }
    
    // MARK: - UITableViewDataSource
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return proyectos.count
    }
    
    func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            // 1. Elimina el registro de tu fuente de datos
            let proyectoAEliminar = proyectos[indexPath.row]
            eliminarProyecto(proyectoAEliminar)

            // 2. Actualiza tu arreglo 'proyectos'
            proyectos.remove(at: indexPath.row)

            // 3. Elimina la fila de la tabla con una animación
            tableView.deleteRows(at: [indexPath], with: .fade)
            
            showToast(message: "Proyecto eliminado")
        }
    }
    
    func eliminarProyecto(_ proyecto: Proyectos) {
        let appDelegate = UIApplication.shared.delegate as! AppDelegate
        let context = appDelegate.persistentContainer.viewContext
        
        context.delete(proyecto)
        
        do {
            try context.save()
        } catch let error as NSError {
            print("Error al eliminar proyecto: \(error), \(error.userInfo)")
        }
    }


    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "celda", for: indexPath)
        let proyecto = proyectos[indexPath.row]
        cell.textLabel?.text = proyecto.nombreProyecto
        cell.detailTextLabel?.text = proyecto.descripcion
        return cell
    }
    
    func showToast(message: String, duration: TimeInterval = 2.5) {
        let toastLabel = UILabel(frame: CGRect(x: self.view.frame.size.width/2 - 150, y: self.view.frame.size.height-150, width: 300, height: 35))
        toastLabel.backgroundColor = UIColor.black.withAlphaComponent(0.6)
        toastLabel.textColor = UIColor.white
        toastLabel.textAlignment = .center;
        toastLabel.font = UIFont(name: "Montserrat-Light", size: 12.0)
        toastLabel.text = message
        toastLabel.alpha = 1.0
        toastLabel.layer.cornerRadius = 10;
        toastLabel.clipsToBounds  =  true
        self.view.addSubview(toastLabel)
        UIView.animate(withDuration: duration, delay: 0.1, options: .curveEaseOut, animations: {
            toastLabel.alpha = 0.0
        }, completion: {(isCompleted) in
            toastLabel.removeFromSuperview()
        })
    }

    
    // MARK: - UITableViewDelegate
    // Implementa aquí otros métodos de UITableViewDelegate si es necesario
}
