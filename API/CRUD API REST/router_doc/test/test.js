let   chai     = require('chai');
let   chaiHttp = require('chai-http');
const expect   = require('chai').expect;
chai.use(chaiHttp);const url= 'http://localhost:8082';
//Encapsular en test dentro de la funcion describe() Y describirmos el test

describe('Inserte un consejo: ',()=>{     
    it('Escribir consejos', (done) => {       
        chai.request(url)   
        .post('/AgregarConsejos')
        .send({ consejo:"La curva de una sonrisa es capaz de enderezar muchas cosas." })
        .end( function(err,res){
            expect(res).to.have.status(200);        
             done();
            }); 
    });
});

describe('Obtiene todos los consejos',()=>{   
    it('Debe obtener todas los consejos.', (done) => {
        chai.request(url)     
        .get('/MostrarConsejos')
        .send()
        .end( function(err,res){
            expect(res).to.have.status(200);   
            expect(res).to.be.json;              
            done();
        });
    });
});