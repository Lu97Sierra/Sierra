const xp = require("express")
const pg = require("pg")

const conString = {
    user: 'root',
    host: '127.0.0.1',
    database: 'L18100233',
    password: 'password'
}

var pgClient = new pg.Client(conString);

const app = xp()

app.use(xp.json())
app.use(xp.text())

app.get('/',function(req,res) {
    pgClient.connect()
    pgClient.query('SELECT * FROM preguntas WHERE ID =' + req.body)
    .then(response =>{
        console.log(response.rows)
        res.send(response.rows)
    })
})

app.listen(1234)