package com.example.a2

import android.os.Bundle
import android.view.LayoutInflater
import android.view.Menu
import android.view.MenuInflater
import android.view.MenuItem
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.core.view.MenuProvider
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.example.a2.databinding.FragmentListaArticulosBinding

class ListaArticulosFragment : Fragment() {
    //public var actualizarLista: Boolean = false
    private var _binding: FragmentListaArticulosBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        _binding = FragmentListaArticulosBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        //MENU
        requireActivity().addMenuProvider(object : MenuProvider {
            override fun onCreateMenu(menu: Menu, menuInflater: MenuInflater) {
                menuInflater.inflate(R.menu.menu_fragment_lista_articulos,menu)
            }

            override fun onMenuItemSelected(menuItem: MenuItem): Boolean {
                return when (menuItem.itemId){
                    R.id.menu_fragment_lista_frutas_to_fragment_frutas ->{
                        findNavController().navigate(R.id.action_ListaArticulosFragment_to_AgregarArituloFragment)
                        true
                    }
                    R.id.menu_fragment_lista_frutas_to_fragment_frutas_verduras ->{
                        findNavController().navigate(R.id.action_ListaArticulosFragment_to_ListaCategoriasFragment)
                        true
                    }
                    else -> false
                }
            }
        }, viewLifecycleOwner)

        binding.recyclerView.adapter = ListaFrutasAdapter({

            EliminarFruta(it)
        })
    }

    fun MostrarArticulo(articulo : Frutas){
        Toast.makeText(context,"Click a ${articulo.nombre}",Toast.LENGTH_SHORT).show()
    }

    fun EliminarFruta(articulo: Frutas){
        val dialog = EliminarArticuloDialogFragment(articulo)
        activity?.let { dialog.show(it.supportFragmentManager, "EliminarFrutaDialogFragment") }
        binding.recyclerView.adapter = ListaFrutasAdapter({

            EliminarFruta(it)
        })
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}