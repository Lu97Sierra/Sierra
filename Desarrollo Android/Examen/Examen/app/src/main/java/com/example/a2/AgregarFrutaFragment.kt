package com.example.a2

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.example.a2.databinding.FragmentAgregarFrutaBinding
import com.example.a2.databinding.FragmentAgregarVerduraBinding
import com.google.android.material.snackbar.Snackbar

class AgregarVerduraFragment : Fragment() {
    private var _binding: FragmentAgregarVerduraBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        _binding = FragmentAgregarVerduraBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding.btnGuardar.setOnClickListener {
            val fruta = Frutas(
                id = binding.editId.text.toString(),
                nombre = binding.editNombre.text.toString(),
                precio = binding.editPrecio.text.toString().toDouble(),
                cantidad = binding.editCantidad.text.toString().toInt()
            )
            Singleton.lista.add(fruta)
            Snackbar.make(it, "Articulo guardado",Snackbar.LENGTH_LONG).show()
            findNavController().navigate(R.id.action_AgregarArituloFragment_to_ListaArticulosFragment)
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}