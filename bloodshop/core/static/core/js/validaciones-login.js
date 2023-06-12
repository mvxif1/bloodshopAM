
$(document).ready(function() {
  $('#form1').submit(function(event) {
    event.preventDefault(); // evitar la acción por defecto del formulario

    var correo = $('#email').val();
    var contraseña = $('#clave').val();
    let msjMostrar = "";
    let enviar = false;

    // verificar que los campos no estén vacíos
    if (correo.trim() === '' || contraseña.trim() === '') {
      alert('Por favor ingrese su nombre de usuario y contraseña.');
      return;

    }
    if (correo.trim()=== correo){

      alert("Su cuenta a sido aceptada correctamente."); 
      $("#submit").attr("href", "http://127.0.0.1:5501/html/inicio-bloodshop.html");

    }

  });
});