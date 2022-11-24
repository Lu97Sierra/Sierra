let   chai     = require('chai');
let   chaiHttp = require('chai-http');
const expect   = require('chai').expect;
chai.use(chaiHttp);const url= 'http://localhost:8081';
//Encapsular en test dentro de la funcion describe() Y describirmos el test

describe('Inserte las respuestas: ',()=>{     
    it('Escribir respuestas', (done) => {       
        chai.request(url)   
        .post('/Respuestas')
        .send({ Nombre:"Gustavo", Pregunta1:"si",Pregunta2:'si' })
        .end( function(err,res){
            expect(res).to.have.status(200);        
            expect(res.text).to.be.a('string');      
             done();
            }); 
    });
});

describe('Obtiene todas las respuestas',()=>{   
    it('Debe obtener todas las respuestas', (done) => {
        chai.request(url)     
        .get('/Respuestas')
        .send()
        .end( function(err,res){
            expect(res).to.have.status(200);   
            expect(res).to.be.json;              
            done();
        });
    });
});