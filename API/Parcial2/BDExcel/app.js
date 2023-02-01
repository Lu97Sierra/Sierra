let json2xls = require('json2xls')
let mysql = require('mysql')
let fs = require('fs')

var con = mysql.createConnection({
    host    :'127.0.0.1',
    user    :'root',
    password:'password',
    database:'L18100233'
});

con.connect();

con.query('SELECT * FROM preguntas', function (error, results, fields) {
    if(error) throw error;

    var xls = json2xls(results);
    fs.writeFileSync(`${__dirname}/excel/data.xlsx`,xls,'binary');
});
con.end();