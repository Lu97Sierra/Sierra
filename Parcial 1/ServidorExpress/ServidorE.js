var express = require('express')
var cors = require('cors')
var fs = require('fs')
var morgan = require('morgan')
var path = require('path')

var app = express()

app.use(cors({origin:"http://localhost"}))
app.use(express.text())
app.use(express.json())

var accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), { flags: 'a' })
app.use(morgan('combined', { stream: accessLogStream }))

/* app.use((res,res,next)=> {
    console.log('Primer mirroware')
    next()
},(res,res,next)=> {
    console.log('Segunda MirrorWare')
    next()
}) */

// app.get('/',(req,res) => {
//     //res.send('Servidor Express contestando a get desde el puerto 8082')
//     res.sendFile('./static/index.html',{root:__dirname},(err)=>{console.log('Archivo enviado')})
// })

app.post('/texto',(req,res) => {
    //res.send('Servidor Express contestando a post desde el puerto 8082')
    //res.json({usuario:'Gustavo'})
    console.log(req.body)
    let say = req.body.toUpperCase()
    let sinesp = req.body.trim()
    let longi = req.body.lenght
    res.json({ mayusculas: may,
               sinespacios: sinesp,
                longitud: longi})
})

app.post('/json',(req,res) => {
    //res.send('Servidor Express contestando a post desde el puerto 8082')
    //res.json({usuario:'Gustavo'})
    console.log(req.body.nombres)
    let cadena = "Hola "+req.body.nombres+" "+req.body.apellido+" como estas"
    res.json({saludo:cadena}) 
})

app.get('/mayusculas/:cadena',(req,res) => {
   console.log(req.params)
   res.send(req.params)
})

app.get('/suma',(req,res) => {
    console.log(res.query)
    let suma = parseInt(req.query.x)+parseInt(req.query.y)
    res.send(`La suma es ${suma}`)
 })

app.use((req,res) => {
    res.status(404).sendFile('./static/Error404.html',{root:__dirname})
})

app.listen(8082,() => {
    console.log('Servidor Express escuchando desde el pto 8082')
    console.log(__dirname)
    console.log(__filename)
})