const express = require('express')
const app = express()

app.get('/',(req,res) => {
    res.end('Servidor Express contestando')
})

app.listen(8081,()=>(console.log('Servidor corriendo y escuchando 8081')))