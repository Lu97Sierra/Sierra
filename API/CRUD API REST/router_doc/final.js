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
* /MostrarConsejos:
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
* /AgregarConsejos:
*  post:
*    description: Envia consejos
*    parameters:
*      - name: consejo
*        in: query
*        description: 'Envia un consejo'
*        schema:
*          type: string
*    responses:
*      200:
*        description: Lista de consejos
*/
router.post('/',(req,res) => {
    console.log(req.query);

    let params = {
        'Consejo': req.query.consejo
    }

    let sql = 'INSERT INTO consejos SET ?';
    let query = con.query(sql,params,(err,result)=>{
        if(err) throw err;
        res.send('Se ha hecho el INSERT')
    });
});

/**  
* @swagger
* /borrarConsejo/{ID}:
*  delete:
*    description: Borra consejos
*    parameters:
*      - name: ID
*        in: path
*        description: Eliminar Consejo
*        required: true
*        schema:
*          type: integer
*          format: int64
*    responses:
*      200:
*        description: Lista de consejos
*/
router.delete('/:ID', (req,res) => {
    let sql = `DELETE FROM consejos WHERE ID=${req.params.ID}`;
    let query = con.query(sql,(err,results) =>{
        if(err) throw err;
        res.send(`Se ha eliminado correctamente el ID= ${req.params.ID}`)
    });
});

/**
  * @swagger
  * /actualizarConsejo/{ID}/{Consejo}:
  *   put:
  *     description: Actualiza el consejo dependiendo el ID que ingreses.
  *     parameters:
  *       - name: ID
  *         in: path
  *         description: 'Se toma el id para poder modificar'
  *         schema:
  *           type: int
  *       - name: Consejo
  *         in: path
  *         description: 'Actualiza el consejo'
  *         schema:
  *           type: string
  *     responses:
  *       200:
  *         description: Retorna el objetos .
  */
   router.put('/:ID/:Consejo', (req, res) => {
    console.log(req.query);
  
    let querys = {
      
      'ID': req.query.ID,
      'Consejo': req.query.Consejo
    }
  
    let sql = `UPDATE consejos SET consejo='${req.params.Consejo}' WHERE ID = ${req.params.ID}`;
  
    let query = con.query(sql,(err,results) =>{
        if(err) throw err;
        res.send(`Se ha actualizado correctamente el ID= ${req.params.ID}`)
    });
  }); 
  

module.exports.router=router
//app.listen(1234, ()=>{console.log('Servidor corriendo...')})