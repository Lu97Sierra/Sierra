const express = require("express")
var mySQL = require("mySQL")
const app = express()

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

app.listen(1234)