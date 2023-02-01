new gridjs.Grid({
    columns: ['ID','Nombre','Pregunta1','Pregunta2','Pregunta3','Pregunta4','Pregunta5','Pregunta6','Pregunta7','Pregunta8'],
    server: {
      url: 'http://127.0.0.1:1234/get', 
      then: data => data.map(preguntas => [preguntas.ID,preguntas.Nombre, preguntas.Pregunta1, preguntas.Pregunta2,
        preguntas.Pregunta3,preguntas.Pregunta4,preguntas.Pregunta5,preguntas.Pregunta6,preguntas.Pregunta7,preguntas.Pregunta8])
    } 
  }).render(document.getElementById("wrapper"));

/*   const grid = new Grid({
    columns: ['Title', 'Director', 'Producer'],
    server: {
      url: 'https://swapi.dev/api/films/',
      then: data => data.results.map(movie => [movie.title, movie.director, movie.producer])
    } 
  }); */


   
  
   