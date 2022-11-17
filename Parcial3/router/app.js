const express = require('express');
const cors    = require('cors');
const ruta_pregunta = require('./CRUD')




const app= express();
app.use(cors({origin:"*"}))
app.use(express.text());
app.use(express.json());

app.use('/pregunta',ruta_pregunta.router);

app.listen(8082, ()=> {
    console.log("Servidor express escuchando en puerto 8082");
})