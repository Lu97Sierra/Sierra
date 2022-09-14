var express = require('express')
var cors = require('cors')

var app = express()
app.use(cors())

app.get('/',(req,res) => {
    res.send('Servidor Express contestando a get desde el puerto 8082')
})

app.post('/',(req,res) => {
    res.send('Servidor Express contestando a post desde el puerto 8082')
})

app.listen(8082,() => {
    console.log('Servidor Express escuchando desde el pto 8082')
})