package com.example.a2

import android.graphics.Color
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView


class ListaFrutasAdapter(val funcion: (Frutas) -> Unit) : RecyclerView.Adapter<ListaFrutasAdapter.ViewHolder>() {

    class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
        val tvId : TextView
        val tvNombre: TextView
        val tvPrecio: TextView
        val tvCantidad: TextView
        init {
            // Define click listener for the ViewHolder's View.
            tvId = view.findViewById(R.id.tvId)
            tvNombre = view.findViewById(R.id.tvNombreVerdura)
            tvPrecio = view.findViewById(R.id.tvPrecio)
            tvCantidad = view.findViewById(R.id.tvCantidad)
        }
    }

    // Create new views (invoked by the layout manager)
    override fun onCreateViewHolder(viewGroup: ViewGroup, viewType: Int): ViewHolder {
        // Create a new view, which defines the UI of the list item
        val view = LayoutInflater.from(viewGroup.context)
            .inflate(R.layout.list_item_view, viewGroup, false)
        return ViewHolder(view)
    }

    // Replace the contents of a view (invoked by the layout manager)
    override fun onBindViewHolder(viewHolder: ViewHolder, position: Int) {
        // Get element from your dataset at this position and replace the
        // contents of the view with that element
        viewHolder.tvId.text = Singleton.lista[position].id
        viewHolder.tvNombre.text = Singleton.lista[position].nombre
        viewHolder.tvPrecio.text = Singleton.lista[position].precio.toString()
        viewHolder.tvCantidad.text = Singleton.lista[position].cantidad.toString()

        if(Singleton.lista[position].cantidad <= 25){
            viewHolder.tvId.setTextColor((Color.RED))
            viewHolder.tvNombre.setTextColor(Color.RED)
        }

        viewHolder.itemView.setOnClickListener {
            funcion(Singleton.lista[position])
        }

    }

    // Return the size of your dataset (invoked by the layout manager)
    override fun getItemCount() = Singleton.lista.size
}
