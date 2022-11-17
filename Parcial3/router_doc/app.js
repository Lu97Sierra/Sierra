const express = require('express');
const cors    = require('cors');
const ruta_pregunta = require('./CRUD')
const swaggerUI = require('swagger-ui-express');
const swaggerJsDoc = require('swagger-jsdoc');

const swaggerOptions = {
    definition: {
    openapi: '3.0.0',
    info: {
    title: 'API Empleados',
    version: '1.0.0',
    },
    servers:[
    {url: "http://localhost:8082"}
    ], 
    },
    apis: [`${path.join(__dirname,"./router_doc/CRUD.js")}`],
    };

const swaggerDocs = swaggerJsDoc(swaggerOptions);
app.use("/api-docs",swaggerUI.serve,swaggerUI.setup(swaggerDocs));

const app= express();
app.use(cors({origin:"http://localhost"}))
app.use(express.text());
app.use(express.json());

app.use('/pregunta',ruta_pregunta.router);

app.listen(8082, ()=> {
    console.log("Servidor express escuchando en puerto 8082");
})