const express = require("express")
var mySQL = require("mySQL")
const app = express()
const cors = require('cors')
app.use(cors({origin:"*"})) //poner un asterico para que pase todo en all
app.use(express.text())
app.use(express.json())

var con = mySQL.createConnection({
    user: 'root',
    host: '127.0.0.1',
    database: 'L18100233',
    password: 'password',
    port: '3306'
});

app.get('/get/:ID',function(req,res) {
    let sql=(`SELECT * FROM preguntas WHERE ID = ${req.params.ID}`);
    let query = con.query(sql,(err,result)=>{
        if(err) throw err;
        res.send(result)
    });
});

app.get('/get',function(req,res) {
    let sql=(`SELECT * FROM preguntas`);
    let query = con.query(sql,(err,result)=>{
        if(err) throw err;
        res.send(result)
    });
});

app.post('/post',(req,res) => {
    console.log(req.query);

    let params = {
        'Nombre': req.query.Nombre,
        'Pregunta1': req.query.Pregunta1,
        'Pregunta2': req.query.Pregunta2,
        'Pregunta3': req.query.Pregunta3,
        'Pregunta4': req.query.Pregunta4,
        'Pregunta5': req.query.Pregunta5,
        'Pregunta6': req.query.Pregunta6,
        'Pregunta7': req.query.Pregunta7,
        'Pregunta8': req.query.Pregunta8
    }

    let sql = 'INSERT INTO preguntas SET ?';
    let query = con.query(sql,params,(err,result)=>{
        if(err) throw err;
        res.send('Se ha hecho el INSERT')
    });
});

app.put('/put/:ID', (req, res) => {
    console.log(req.query);

    let querys = {
        'Nombre': req.query.Nombre,
        'Pregunta1': req.query.Pregunta1,
        'Pregunta2': req.query.Pregunta2,
        'Pregunta3': req.query.Pregunta3,
        'Pregunta4': req.query.Pregunta4,
        'Pregunta5': req.query.Pregunta5,
        'Pregunta6': req.query.Pregunta6,
        'Pregunta7': req.query.Pregunta7,
        'Pregunta8': req.query.Pregunta8
    }
    let sql = `UPDATE preguntas SET ? WHERE ID= ${req.params.ID}`;

    let query = con.query(sql,querys,(err,results) =>{
        if(err) throw err;
        res.send('Se ha hecho el UPDATE')
    });
});

app.delete('/delete/:ID', (req,res) => {
    let sql = `DELETE FROM preguntas WHERE ID= ${req.params.ID}`;
    let query = con.query(sql,(err,results) =>{
        if(err) throw err;
        res.send(`Se ha eliminado correctamente el ID: ${req.params.ID}`)
    });
});

app.listen(1234, ()=>{console.log('Servidor corriendo...')})