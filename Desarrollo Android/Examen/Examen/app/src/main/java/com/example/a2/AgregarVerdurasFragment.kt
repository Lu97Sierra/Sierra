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

class AgregarCategoriaFragment : Fragment() {
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
            val nombrecat = binding.editNombre.text.toString()
            Singleton.listFruta.add(nombrecat)
            Snackbar.make(it, "Fruta guardada", Snackbar.LENGTH_LONG).show()
            findNavController().navigate(R.id.action_AgregarCategoriaFragment_to_ListaCategoriasFragment)
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}