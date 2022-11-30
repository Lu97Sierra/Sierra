const express = require("express")
var mySQL = require("mySQL")
const app = express()
const cors = require('cors')
app.use(cors({origin:"*"})) //poner un asterico para que pase todo en all
app.use(express.text())
app.use(express.json())

var router = express.Router()

var con = mySQL.createConnection({
    user: 'root',
    host: '127.0.0.1',
    database: 'L18100233',
    password: 'password',
    port: '3306'
});

router.get('/get/:ID',function(req,res) {
    let sql=(`SELECT * FROM consejos WHERE ID = ${req.params.ID}`);
    let query = con.query(sql,(err,result)=>{
        if(err) throw err;
        res.send(result)
    });
});

/**  
* @swagger
* /consejo:
*  get:
*    description: Obtiene consejos
*    responses:
*      200:
*        description: Lista de consejos
*        content:
*          application/json:
*            schema:
*              type: string
*              items:
*/

router.get('/',function(req,res) {
    let sql=(`SELECT * FROM consejos`);
    let query = con.query(sql,(err,result)=>{
        if(err) throw err;
        res.send(result)
    });
});


/**  
* @swagger
* /EnviarConsejo:
*  get:
*    description: Obtiene consejos
*    responses:
*      200:
*        description: Lista de consejos
*        content:
*          application/json:
*            schema:
*              type: string
*              items:
*/
router.post('/post',(req,res) => {
    console.log(req.query);

    let params = {
        'consejo': req.query.consejo,
    }

    let sql = 'INSERT INTO consejos SET ?';
    let query = con.query(sql,params,(err,result)=>{
        if(err) throw err;
        res.send('Se ha hecho el INSERT')
    });
});

router.put('/put/:ID', (req, res) => {
    console.log(req.query);

    let querys = {
        'consejo': req.query.consejo,
    }
    let sql = `UPDATE consejos SET ? WHERE ID= ${req.params.ID}`;

    let query = con.query(sql,querys,(err,results) =>{
        if(err) throw err;
        res.send('Se ha hecho el UPDATE')
    });
});

router.delete('/delete/:ID', (req,res) => {
    let sql = `DELETE FROM consejos WHERE ID= ${req.params.ID}`;
    let query = con.query(sql,(err,results) =>{
        if(err) throw err;
        res.send(`Se ha eliminado correctamente el ID: ${req.params.ID}`)
    });
});

module.exports.router=router
//app.listen(1234, ()=>{console.log('Servidor corriendo...')})