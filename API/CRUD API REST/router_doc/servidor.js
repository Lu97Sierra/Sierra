const express = require('express')
const app = express()
const {query}= require('express')
const cors = require('cors')
const ruta_consejo = require('./final.js')
const path=require('path')


const swaggerUI     = require('swagger-ui-express');
const swaggerJsDoc  = require('swagger-jsdoc');

const swaggerOptions = {definition:{
    openapi: '3.0.0',
     info: {title: 'API Consejos',
     version: '1.0.0',      
    },
    servers:[{url: "http://localhost:8082"}],  
    },
    apis: [`${path.join(__dirname,"./final.js")}`],
  };


app.use(express.json())
app.use(express.text())
app.use(cors({ origin:"*"}))

app.use('/MostrarConsejos',ruta_consejo.router);
app.use('/MostrarConsejos/',ruta_consejo.router);
app.use('/AgregarConsejos',ruta_consejo.router);
app.use('/actualizarConsejo',ruta_consejo.router);
app.use('/borrarConsejo',ruta_consejo.router);

const swaggerDocs = swaggerJsDoc(swaggerOptions);
app.use("/api-docs",swaggerUI.serve,swaggerUI.setup(swaggerDocs));


app.listen(8082, ()=>{console.log('Servidor corriendo express')})