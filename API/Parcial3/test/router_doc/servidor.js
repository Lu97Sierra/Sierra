const express = require('express')
const app = express()
const {query}= require('express')
const cors = require('cors')
const ruta_respuesta = require('./CRUD')
const path=require('path')


const swaggerUI     = require('swagger-ui-express');
const swaggerJsDoc  = require('swagger-jsdoc');

const swaggerOptions = {definition:{
    openapi: '3.0.0',
     info: {title: 'API Preguntas',
     version: '1.0.0',      
    },
    servers:[{url: "http://localhost:8082"}],  
    },
    apis: [`${path.join(__dirname,"./CRUD.js")}`],
  };


app.use(express.json())
app.use(express.text())
app.use(cors({ origin:"http://localhost"}))

app.use('/MostrarRespuestas',ruta_respuesta.router);
app.use('/MostrarRespuestas/',ruta_respuesta.router);
app.use('/AgregarRespuestas',ruta_respuesta.router);
app.use('/actualizarRespuesta/',ruta_respuesta.router);
app.use('/borrarRespuestas/',ruta_respuesta.router);

const swaggerDocs = swaggerJsDoc(swaggerOptions);
app.use("/api-docs",swaggerUI.serve,swaggerUI.setup(swaggerDocs));


app.listen(8082, ()=>{console.log('Servidor corriendo express')})