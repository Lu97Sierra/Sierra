//
//  ViewController.swift
//  Practica 1
//
//  Created by Gustavo on 01/12/23.
//  Copyright © 2023 Gustavo. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBOutlet weak var sumaTextField: UITextField!
    @IBOutlet weak var diferenciaTextField: UITextField!
    @IBOutlet weak var resultadoLabel: UILabel!
    

    @IBAction func calcularNumeros(_ sender: Any) {
        if let suma = Double(sumaTextField.text!), let diferencia = Double(diferenciaTextField.text!){
            let a = (suma + diferencia) / 2
            let b = suma - a
            resultadoLabel.text = "Resultado: Numero a: \(a) , Numero b: \(b)"
        } else {
            resultadoLabel.text = "Ingrese numeros validos, por favor."
        }
    }
    
}

