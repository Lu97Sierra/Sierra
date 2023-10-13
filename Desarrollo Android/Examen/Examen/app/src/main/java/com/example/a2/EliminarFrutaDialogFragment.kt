package com.example.a2

import android.app.Dialog
import android.content.DialogInterface
import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AlertDialog
import androidx.fragment.app.DialogFragment

class EliminarArticuloDialogFragment(val fruta: Frutas) : DialogFragment() {

    override fun onCreateDialog(savedInstanceState: Bundle?): Dialog {
        Log.d("Eliminar Fruta", "EliminarFrutaDialogFragments.onCreateDialog")
        return activity?.let {
            // Use the Builder class for convenient dialog construction
            val builder = AlertDialog.Builder(it)
            builder.setMessage("¿Desea eliminar fruta: ${fruta.nombre}?")
                .setPositiveButton("Si",
                    DialogInterface.OnClickListener { dialog, id ->
                        Singleton.lista.remove(fruta)
                        //funcion(articulo)
                    })
                .setNegativeButton("No",
                    DialogInterface.OnClickListener { dialog, id ->
                        // User cancelled the dialog
                    })
            // Create the AlertDialog object and return it
            builder.create()
        } ?: throw IllegalStateException("Activity cannot be null")
    }
}