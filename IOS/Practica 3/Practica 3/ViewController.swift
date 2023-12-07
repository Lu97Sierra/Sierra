//
//  ViewController.swift
//  Practica 3
//
//  Created by Gustavo on 01/12/23.
//  Copyright © 2023 Gustavo. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var colorView: UIView!
    @IBOutlet weak var hexTextField: UITextField!
    @IBOutlet weak var redSlider: UISlider!
    @IBOutlet weak var greenSlider: UISlider!
    @IBOutlet weak var blueSlider: UISlider!
    @IBOutlet weak var colorModeSwitch: UISwitch!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func colorModeChanged(_ sender: UISwitch) {
        hexTextField.isEnabled = !sender.isOn
        redSlider.isEnabled = sender.isOn
        greenSlider.isEnabled = sender.isOn
        blueSlider.isEnabled = sender.isOn
        
        if sender.isOn {
            updateColorViewFromSliders()
        }
    }
    
    @IBAction func applyHexColor(_ sender: UIButton) {
        if let hexColor = hexTextField.text, let color = UIColor(hex: hexColor) {
            colorView.backgroundColor = color
            updateSlidersWithColor(color: color)
        }
    }
    
    @IBAction func sliderValueChanged(_ sender: UISlider) {
        updateColorViewFromSliders()
        updateHexValueInTextField()
    }
    
    func updateHexValueInTextField() {
        let redHex = String(format: "%02X", Int(redSlider.value))
        let greenHex = String(format: "%02X", Int(greenSlider.value))
        let blueHex = String(format: "%02X", Int(blueSlider.value))
        hexTextField.text = "\(redHex)\(greenHex)\(blueHex)"
    }

    func updateColorViewFromSliders() {
        if colorModeSwitch.isOn {
            colorView.backgroundColor = UIColor(
                redInt: Int(redSlider.value),
                greenInt: Int(greenSlider.value),
                blueInt: Int(blueSlider.value)
            )
        }
    }
    

    func updateSlidersWithColor(color: UIColor) {
        // Descomponer el color en sus componentes RGB
        var red: CGFloat = 0
        var green: CGFloat = 0
        var blue: CGFloat = 0
        color.getRed(&red, green: &green, blue: &blue, alpha: nil)

        // Actualizar los sliders con los nuevos valores
        redSlider.value = Float(red * 255.0)
        greenSlider.value = Float(green * 255.0)
        blueSlider.value = Float(blue * 255.0)
    }
    
    
}

extension UIColor {
    convenience init?(hex: String) {
        guard hex.count == 6, hex.range(of: "^[0-9A-Fa-f]{6}$", options: .regularExpression) != nil else {
            return nil
        }
        
        var rgbValue: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&rgbValue)
        
        let red = CGFloat((rgbValue & 0xFF0000) >> 16) / 255.0
        let green = CGFloat((rgbValue & 0x00FF00) >> 8) / 255.0
        let blue = CGFloat(rgbValue & 0x0000FF) / 255.0
        
        self.init(red: red, green: green, blue: blue, alpha: 1.0)
    }
    
    convenience init(redInt: Int, greenInt: Int, blueInt: Int) {
        self.init(
            red : CGFloat(redInt) / 255.0,
            green : CGFloat(greenInt) / 255.0,
            blue: CGFloat(blueInt) / 255.0,
            alpha : 1.0
        )
    }
}

extension UISlider {
    var hexValue: String {
        return String(format: "%02X", Int(self.value))
    }
}
