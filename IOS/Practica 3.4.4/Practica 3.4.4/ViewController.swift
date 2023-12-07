//
//  ViewController.swift
//  Practica 3.4.4
//
//  Created by Gustavo on 07/12/23.
//  Copyright © 2023 Gustavo. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UIPickerViewDataSource, UIPickerViewDelegate {

    @IBOutlet weak var shapePickerView: UIPickerView!
    @IBOutlet weak var resultLabel: UILabel!
    
    let shapes = ["Cuadrado", "Triángulo", "Rectángulo", "Círculo", "Pentágono"]

    override func viewDidLoad() {
        super.viewDidLoad()
        
        shapePickerView.dataSource = self
        shapePickerView.delegate = self
    }

    // Número de columnas de datos
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }

    // Número de filas de datos
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return shapes.count
    }

    // El dato a retornar para la fila y componente (columna) que está siendo pasada
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        return shapes[row]
    }
    
    // Acción al seleccionar una fila
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        // Tu código aquí, por ejemplo, puedes actualizar una etiqueta con la forma seleccionada
        print(shapes[row])
    }
    
    // ... tu código existente ...

    @IBAction func calculatePerimeter(_ sender: UIBarButtonItem) {
        showAlert(forCalculation: "Perímetro")
    }

    @IBAction func calculateArea(_ sender: UIBarButtonItem) {
        showAlert(forCalculation: "Área")
    }

    @IBAction func calculateVolume(_ sender: UIBarButtonItem) {
        showAlert(forCalculation: "Volumen")
    }

    func showAlert(forCalculation calculationType: String) {
        let selectedShape = shapes[shapePickerView.selectedRow(inComponent: 0)]

        // Crear alerta
        let alert = UIAlertController(title: "Calcular \(calculationType) de \(selectedShape)", message: "Introduce los valores necesarios", preferredStyle: .alert)

        // Configurar text fields según la figura y el cálculo
        switch selectedShape {
            case "Cuadrado":
                let placeholder = calculationType == "Volumen" ? "Introduce la longitud del lado del cuadrado" : "Introduce la longitud del lado del cuadrado"
                alert.addTextField { textField in
                    textField.placeholder = placeholder
                }
                if calculationType == "Volumen" {
                    alert.addTextField { textField in
                        textField.placeholder = "Introduce la altura del prisma (opcional)"
                    }
                }

            case "Triángulo":
                alert.addTextField { textField in
                    textField.placeholder = "Introduce la longitud del lado del triángulo"
                }
                alert.addTextField { textField in
                    textField.placeholder = "Introduce la longitud de la base del triángulo"
                }
                if calculationType != "Perímetro" {
                    alert.addTextField { textField in
                        textField.placeholder = "Introduce la altura del triángulo"
                    }
                }

            case "Rectángulo":
                alert.addTextField { textField in
                    textField.placeholder = "Introduce la longitud del rectángulo"
                }
                alert.addTextField { textField in
                    textField.placeholder = "Introduce la anchura del rectángulo"
                }
                if calculationType == "Volumen" {
                    alert.addTextField { textField in
                        textField.placeholder = "Introduce la altura del prisma"
                    }
                }

            case "Círculo":
                alert.addTextField { textField in
                    textField.placeholder = "Introduce el radio del círculo"
                }

            case "Pentágono":
                alert.addTextField { textField in
                    textField.placeholder = "Introduce el lado del pentágono"
                }
                if calculationType != "Perímetro" {
                    alert.addTextField { textField in
                        textField.placeholder = "Introduce la apotema del pentágono"
                    }
                }
                if calculationType == "Volumen" {
                    alert.addTextField { textField in
                        textField.placeholder = "Introduce la altura del prisma"
                    }
                }
            default:
                break
        }
        
        // Acción para realizar el cálculo
        let calculateAction = UIAlertAction(title: "Calcular", style: .default) { [weak self] _ in
            let textFields = alert.textFields?.compactMap { $0.text }.compactMap { Double($0) }
            guard let values = textFields, !values.isEmpty else {
                self?.resultLabel.text = "Por favor, ingrese valores numéricos válidos."
                return
            }

            let result: Double
            switch selectedShape {
            case "Cuadrado":
                result = self?.calculateResult(forShape: selectedShape, calculationType: calculationType, values: values) ?? 0

            case "Triángulo":
                result = self?.calculateResult(forShape: selectedShape, calculationType: calculationType, values: values) ?? 0

            case "Rectángulo":
                result = self?.calculateResult(forShape: selectedShape, calculationType: calculationType, values: values) ?? 0

            case "Círculo":
                result = self?.calculateResult(forShape: selectedShape, calculationType: calculationType, values: values) ?? 0

            case "Pentágono":
                result = self?.calculateResult(forShape: selectedShape, calculationType: calculationType, values: values) ?? 0

            default:
                result = 0
            }

            self?.updateResultLabel(with: result, forCalculationType: calculationType, values: values)
        }
        
        alert.addAction(calculateAction)
        
        // Mostrar alerta
        present(alert, animated: true, completion: nil)
    }

    func calculateResult(forShape shape: String, calculationType: String, values: [Double]) -> Double {
        switch shape {
        case "Cuadrado":
            let cuadrado = Cuadrado(lado: values[0])
            return performCalculation(calculationType, for: cuadrado)

        case "Triángulo":
            let triangulo = TrianguloIsosceles(lado: values[0], base: values[1], alturaPrisma: values.count > 2 ? values[2] : 0)
            return performCalculation(calculationType, for: triangulo)

        case "Rectángulo":
            let rectangulo = Rectangulo(largo: values[0], ancho: values[1], altura: values.count > 2 ? values[2] : 0)
            return performCalculation(calculationType, for: rectangulo)

        case "Círculo":
            let circulo = Circulo(radio: values[0])
            return performCalculation(calculationType, for: circulo)

        case "Pentágono":
            let pentagono = Pentagono(lado: values[0], apotema: values[1], altura: values.count > 2 ? values[2] : 0)
            return performCalculation(calculationType, for: pentagono)

        default:
            return 0
        }
    }
    
    func performCalculation(_ calculationType: String, for figura: Figura) -> Double {
        switch calculationType {
        case "Perímetro":
            return figura.calcularPerimetro()
        case "Área":
            return figura.calcularArea()
        case "Volumen":
            return figura.calcularVolumen()
        default:
            return 0
        }
    }


    func updateResultLabel(with result: Double, forCalculationType calculationType: String, values: [Double]) {
        // Actualiza la etiqueta con el resultado y los valores de entrada
        let valuesString = values.map { String($0) }.joined(separator: ", ")
        resultLabel.text = "\(calculationType) del \(shapes[shapePickerView.selectedRow(inComponent: 0)]): \(result) (con valores: \(valuesString))"
    }

    
}

// Definir un protocolo con los métodos requeridos
protocol Figura {
    func calcularPerimetro() -> Double
    func calcularArea() -> Double
    func calcularVolumen() -> Double
}

// Crear una clase para cada figura que implemente el protocolo
class Circulo: Figura {
    var radio: Double

    init(radio: Double) {
        self.radio = radio
    }

    func calcularPerimetro() -> Double {
        return 2 * .pi * radio
    }

    func calcularArea() -> Double {
        return .pi * pow(radio, 2)
    }

    func calcularVolumen() -> Double {
        // Para un círculo, volumen no aplica. Puede devolver 0 o quizás nil si cambias el método para devolver un opcional.
        return (4.0 / 3.0) * .pi * pow(radio, 3)
    }
}

class Cuadrado: Figura {
    var lado: Double

    init(lado: Double) {
        self.lado = lado
    }

    func calcularPerimetro() -> Double {
        return lado * 4
    }

    func calcularArea() -> Double {
        return pow(lado, 2)
    }

    func calcularVolumen() -> Double {
        // Para un cuadrado, volumen no aplica. Puede devolver 0 o quizás nil si cambias el método para devolver un opcional.
        return pow(lado,3)
    }
}

class TrianguloIsosceles: Figura {
    var lado: Double // Los dos lados iguales
    var base: Double // La base, que es diferente en un triángulo isósceles
    var alturaPrisma: Double? // La altura del prisma

    // Constructor que toma los dos lados iguales y la base
    init(lado: Double, base: Double) {
        self.lado = lado
        self.base = base
        self.alturaPrisma = nil
    }
    
    init(lado: Double, base: Double, alturaPrisma: Double) {
        self.lado = lado
        self.base = base
        self.alturaPrisma = alturaPrisma
    }

    func calcularPerimetro() -> Double {
        // Perímetro es la suma de los tres lados
        return 2 * lado + base
    }

    func calcularArea() -> Double {
        // Área se calcula con la base y la altura. La altura se deriva del teorema de Pitágoras.
        let altura = sqrt(pow(lado, 2) - pow(base / 2, 2))
        return (base * altura) / 2
    }

    func calcularVolumen() -> Double {
        // Volumen del prisma = Área de la base * Altura del prisma
        let areaBase = calcularArea()
        return areaBase * alturaPrisma!
    }
}

class Rectangulo: Figura {
    var largo: Double
    var ancho: Double
    var altura: Double? // La altura es opcional, solo se usa para calcular el volumen del prisma

    // Constructor para un rectángulo plano (2D)
    init(largo: Double, ancho: Double) {
        self.largo = largo
        self.ancho = ancho
        self.altura = nil
    }

    // Constructor para un prisma rectangular (3D)
    init(largo: Double, ancho: Double, altura: Double) {
        self.largo = largo
        self.ancho = ancho
        self.altura = altura
    }

    func calcularPerimetro() -> Double {
        // Perímetro del rectángulo
        return 2 * (largo + ancho)
    }

    func calcularArea() -> Double {
        // Área del rectángulo
        return largo * ancho
    }

    func calcularVolumen() -> Double {
        // Volumen del prisma rectangular (si se proporciona la altura)
        guard let altura = altura else {
            return 0 // Si no hay altura, no se puede calcular el volumen
        }
        return calcularArea() * altura
    }
}

class Pentagono: Figura {
    var lado: Double
    var apotema: Double
    var altura: Double? // La altura del prisma, opcional para un pentágono regular

    // Constructor para un pentágono regular
    init(lado: Double, apotema: Double) {
        self.lado = lado
        self.apotema = apotema
        self.altura = nil
    }

    // Constructor para un prisma con base de pentágono regular
    init(lado: Double, apotema: Double, altura: Double) {
        self.lado = lado
        self.apotema = apotema
        self.altura = altura
    }

    func calcularPerimetro() -> Double {
        // Perímetro del pentágono
        return 5 * lado
    }

    func calcularArea() -> Double {
        // Área del pentágono regular
        return (5 * lado * apotema) / 2
    }

    func calcularVolumen() -> Double {
        // Volumen del prisma con base de pentágono regular (si se proporciona la altura)
        guard let altura = altura else {
            return 0 // Si no hay altura, no se puede calcular el volumen
        }
        return calcularArea() * altura
    }
}





