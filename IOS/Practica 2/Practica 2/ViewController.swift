//
//  ViewController.swift
//  Practica 2
//
//  Created by Gustavo on 01/12/23.
//  Copyright © 2023 Gustavo. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    // Oultlets
    @IBOutlet weak var altoTextField: UITextField!
    @IBOutlet weak var anchoTextField: UITextField!
    @IBOutlet weak var xTextField: UITextField!
    @IBOutlet weak var yTextField: UITextField!
    @IBOutlet weak var aLabel: UILabel!
    @IBOutlet weak var bLabel: UILabel!
    @IBOutlet weak var resultadoLabel: UILabel!
    
    //Esta variable retendra la instancia de FIguraL
    var figura: FiguraL?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    @IBAction func calcularPerimetro(_ sender: Any) {
        actualizarFigura()
        if let perimetro = figura?.calcularPerimetro() {
            resultadoLabel.text = "Perimetro: \(perimetro)"
        }
    }
    
    @IBAction func calcularArea(_ sender: Any) {
        actualizarFigura()
        if let area = figura?.calcularArea() {
            resultadoLabel.text = "Area: \(area)"
        }
    }
    
    // Funcion para actualizar la figura con los valores de los text field
    func actualizarFigura() {
        if let alto = Double(altoTextField.text!),
            let ancho = Double(anchoTextField.text!),
            let x = Double(xTextField.text!),
            let y = Double(yTextField.text!) {
            figura = FiguraL(alto: alto, ancho: ancho, x: x, y: y)
            aLabel.text = "a: \(figura!.a)"
            bLabel.text = "b: \(figura!.b)"
        } else {
            resultadoLabel.text = "Ingrese valores numericos validos."
        }
    }
    
    


}

class FiguraL {
    var alto: Double
    var ancho: Double
    var x: Double
    var y: Double
    
    var a: Double{
        return alto * ancho
    }
    
    var b: Double{
        return x + y
    }
    
    init(alto: Double, ancho: Double, x: Double, y: Double){
        self.alto = alto
        self.ancho = ancho
        self.x = x
        self.y = y
    }
    
    func calcularPerimetro() -> Double {
        return 2 * (alto + ancho)
    }
    
    func calcularArea() -> Double {
        return (ancho * y) + ((alto - y) * x)
    }
    
}
