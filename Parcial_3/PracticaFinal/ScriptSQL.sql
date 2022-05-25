create database L18100233;
use L18100233;

create table preguntas
(
ID smallint auto_increment not null,
Nombre varchar(255),
Pregunta1 varchar(255),
Pregunta2 varchar(255),
Pregunta3 varchar(255),
Pregunta4 varchar(255),
Pregunta5 varchar(255),
Pregunta6 varchar(255),
Pregunta7 varchar(255),
Pregunta8 varchar(255),
PRIMARY KEY(ID)
);

insert into preguntas (Nombre,Pregunta1,Pregunta2,Pregunta3,Pregunta4,Pregunta5,Pregunta6,Pregunta7,Pregunta8)
values
('Luis Gustavo','Un medio ambiente limpio es fuente de satisfacción',
'Cuidar el medio ambiente es cuidarnos a nosotros mismos, uno no está separado del otro',
'Ahorrar recursos con los que tengas contacto diario','Reciclaje de papel, Reciclaje de vidrio',
'Reducir los envases o productos de usar y tirar',
'Compra solo lo que necesitas','Las pérdidas de alimentos conllevan el desperdicio de recursos utilizados en la producción como tierra, 
agua, energía e insumos','Los voluntarios se encargan de recoger todos los residuos que puedan de las playas y, de ser posible, identificarlos 
para que estos sean reciclados');