package com.example.a2

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class ListaCategoriasAdapter() : RecyclerView.Adapter<ListaCategoriasAdapter.ViewHolder>() {
    class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
        val tvNombreVerdura: TextView
        init {
            // Define click listener for the ViewHolder's View.
            tvNombreVerdura = view.findViewById(R.id.tvNombreVerdura)
        }
    }

    // Create new views (invoked by the layout manager)
    override fun onCreateViewHolder(viewGroup: ViewGroup, viewType: Int): ViewHolder {
        // Create a new view, which defines the UI of the list item
        val view = LayoutInflater.from(viewGroup.context)
            .inflate(R.layout.list_frutas_item_view, viewGroup, false)
        return ViewHolder(view)
    }

    // Replace the contents of a view (invoked by the layout manager)
    override fun onBindViewHolder(viewHolder: ViewHolder, position: Int) {
        viewHolder.tvNombreVerdura.text = Singleton.listFruta[position].toString()
    }

    // Return the size of your dataset (invoked by the layout manager)
    override fun getItemCount() = Singleton.listFruta.size
}