var express = require('express')
var cors = require('cors')

var app = express()
app.use(cors({origin:"http://localhost"}))

app.get('/',(req,res) => {
    //res.send('Servidor Express contestando a get desde el puerto 8082')
    res.sendFile('./static/index.html',{root:__dirname},(err)=>{console.log('Archivo enviado')})
})

app.post('/',(req,res) => {
    //res.send('Servidor Express contestando a post desde el puerto 8082')
    res.json({usuario:'Gustavo'})
})

app.use((req,res) => {
    res.status(404).sendFile('./static/Error404.html',{root:__dirname})
})

app.listen(8082,() => {
    console.log('Servidor Express escuchando desde el pto 8082')
    console.log(__dirname)
    console.log(__filename)
})