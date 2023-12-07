//
//  preferenciasViewController.swift
//  Proyecto Final v2
//
//  Created by Gustavo on 06/12/23.
//  Copyright © 2023 Gustavo. All rights reserved.
//

import UIKit

class preferenciasViewController: UIViewController {
    

    
    @IBOutlet weak var darkModeSwitch: UISwitch!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Configuración inicial del switch basada en el estilo de interfaz de usuario actual
        if self.traitCollection.userInterfaceStyle == .dark {
            // Interfaz en modo oscuro, encender el switch
            darkModeSwitch.isOn = true
        } else {
            // Interfaz en modo claro, apagar el switch
            darkModeSwitch.isOn = false
        }
    }


    
    @IBAction func darkModeSwitchChanged(_ sender: UISwitch) {
        if sender.isOn {
            // Activar modo oscuro para toda la aplicación
            UIApplication.shared.windows.forEach { window in
                window.overrideUserInterfaceStyle = .dark
            }
        } else {
            // Activar modo claro para toda la aplicación
            UIApplication.shared.windows.forEach { window in
                window.overrideUserInterfaceStyle = .light
            }
        }
    }



}


