$(document).ready(function () {
    $("#form").submit(function (e) {
        e.preventDefault();
        var nombre = $("#nombre").val();
        var apellido = $("#apellido").val();
        var rut = $("#rut").val();

        let msjMostrar = "";
        let enviarnom = false;

        let msjMostrar2 = "";
        let enviarape = false;

        let msjMostrar3 = "";
        let enviarclav = false;


        //Aqui estan las validaciones de el nombre
        if (nombre == '') {
            msjMostrar += ("Por favor, ingrese su nombre");
            enviarnom = true;
        }
        if (nombre.trim().length < 3 || nombre.trim().length > 12) {
            msjMostrar += "*El nombre debe tener entre 3 y 12 caracteres";
            enviarnom = true;
        }

        var letra = nombre.trim().charAt(0);
        if (!esMayuscula(letra)) {
            msjMostrar += "<br>*El nombre debe comenzar con mayúscula";
            enviarnom = true;

        }

        if (!/^[a-zA-Z\s]*$/.test(nombre)) {
            msjMostrar += ("<br>*El nombre solo debe contener letras");
            enviarnom = true;
        }
        if (enviarnom) {
            $("#incompleto").css("color", "red");
            $("#incompleto").html(msjMostrar);

        }
        else {
            $("#incompleto").css("color", "green");
            $("#incompleto").html("Completado");
        }


        //Aqui estan las validaciones de el apellido
        if (apellido.trim().length < 4 || apellido.trim().length > 12) {
            msjMostrar2 += "*El apellido debe tener entre 4 y 12 caracteres";
            enviarape = true;
        }

        var letra = apellido.trim().charAt(0);
        if (!esMayuscula(letra)) {
            msjMostrar2 += ("<br>El apellido debe comenzar con mayúscula");
            enviarape = true;

        }
        if (!/^[a-zA-Z\s]*$/.test(apellido)) {
            msjMostrar2 += ("<br>El apellido solo debe contener letras");
            enviarape = true;
        }

        if (enviarape) {
            $("#incompleto2").css("color", "red");
            $("#incompleto2").html(msjMostrar2);

        }
        else {
            $("#incompleto2").css("color", "green");
            $("#incompleto2").html("Completado");
        }

        //Aqui estan las validaciones de el rut
        var Fn = {
            // Valida el rut con su cadena completa "XXXXXXXX-X"
            validaRut: function (rutCompleto) {
                rutCompleto = rutCompleto.replace("‐", "-");

                if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto))
                    return false;
                var tmp = rutCompleto.split('-');
                var digv = tmp[1];
                var rut = tmp[0];
                if (digv == 'K') digv = 'k';

                return (Fn.dv(rut) == digv);
            },
            dv: function (T) {
                var M = 0, S = 1;
                for (; T; T = Math.floor(T / 10))
                    S = (S + T % 10 * (9 - M++ % 6)) % 11;
                return S ? S - 1 : 'k';
            }
        }
        if (Fn.validaRut($("#rut").val())) {
            $("#msgerror").css("color", "green");
            $("#msgerror").html("Completado");
        } else {
            $("#msgerror").css("color", "red");
            $("#msgerror").html("*El Rut no es válido");

        }

        //Validar Contraseña

        var password = $("#clave").val();
        var mayuscula = /[A-Z]/.test(password);
        var minuscula = /[a-z]/.test(password);
        var numero = /[0-9]/.test(password);

        if (!mayuscula) {
            msjMostrar3 += ("La contraseña debe contener al menos una letra mayúscula.");
            enviarclav = true;
        }

        if (!minuscula) {
            msjMostrar3 += ('<br>La contraseña debe contener al menos una letra minúscula.');
            enviarclav = true;
        }

        if (!numero) {
            msjMostrar3 += ("<br>La contraseña debe contener al menos un número.");
            enviarclav = true;
        }

        if (password.length < 8) {
            msjMostrar3 += ("<br>La contraseña debe tener al menos 8 caracteres.");
            enviarclav = true;
        }

        if (enviarclav) {
            $("#incompleto3").css("color", "red");
            $("#incompleto3").html(msjMostrar3);

        }
        else {
            $("#incompleto3").css("color", "green");
            $("#incompleto3").html("Completado");
        }

        if (enviarnom == false && enviarape == false && enviarclav == false) {
            alert("El formulario de registro se envio correctamente");
        }
        if (correo.trim() === '' || contraseña.trim() === '') {
            alert('Por favor ingrese su nombre de usuario y contraseña.');
            return;
          }


    });
    function esMayuscula(letra) {
        console.log("Estoy aqui");
        console.log(letra);
        console.log(letra.toUpperCase());

        if (letra == letra.toUpperCase()) {
            return true;
        }
        else {
            return false;
        }
    }


});