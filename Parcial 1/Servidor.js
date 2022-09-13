const http = require('http');

const servidor = http.createServer((req,res) => {
    res.end('Servidor HTTP NodeJs esta encendido.');
});

servidor.listen(8081);