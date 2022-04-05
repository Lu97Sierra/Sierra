/* Con Javascript */
/* const btnToggle = document.querySelector('.toggle-btn');

btnToggle.addEventListener('click', function () {
    
  document.getElementById('sidebar').classList.toggle('active');
  
}); */

// Con JQuery 
$(document).ready(function(){
    $(".toggle-btn").click(alternarMenu);
    function alternarMenu(){
    $("#sidebar").toggleClass("active");
    }
});