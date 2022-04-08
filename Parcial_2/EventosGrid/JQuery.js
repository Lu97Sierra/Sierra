$(document).ready(function(){
    $(".toggle-btn").click(alternarMenu);
    function alternarMenu(){
    $("#sidebar").toggleClass("active");
    }
});