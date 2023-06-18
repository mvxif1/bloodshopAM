$(document).ready(function () {
    $("#form").submit(function (e) {
        e.preventDefault();
        var apellido = $("#apellido").val();
        var rut = $("#rut").val();
        var fechaNacimiento = new Date($("#fechnac").val());
        var numero = $("#telefono").val();
        var correo = $("#email").val();
        
        let msjMostrar = "";
        let enviarnom = false;

        let msjMostrar2 = "";
        let enviarape = false;

        let msjMostrar3 = "";
        let enviarclav = false;

        let msjMostrar4 = "";
        let enviarfech = false;

        let msjMostrar5 = "";
        let enviartel = false;

        let msjMostrar6 = "";
        let enviarcorreo = false;

        let msjMostrar7 = "";
        let enviarconfcorreo = false;

        let msjMostrar8 = "";
        let enviarconfclave = false;

        //Aqui estan las validaciones de el nombre
        
        var nombre = $("#nombre").val();
        var regex = /^[a-zA-Z0-9\s]+$/;

        if (nombre.trim() === '') {
            msjMostrar += ("Por favor, ingrese su nombre");
            enviarnom = true;
        }

        if (nombre.trim().length < 3) {
            msjMostrar += ("<br>El nombre debe tener al menos 3 caracteres");
            enviarnom = true;
        }
        
        if (!regex.test(nombre)) {
            msjMostrar += ("<br>El nombre no puede contener caracteres especiales");
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
        if (apellido.trim() === '') {
            msjMostrar2 += ("Porfavor, ingrese su apellido");
            enviarape = true;

        }
        
        if (apellido.trim().length < 3) {
            msjMostrar2 += ("<br>El apellido debe tener al menos 3 caracteres");
            enviarape = true;
        }

        
        if (!regex.test(apellido))  {
            msjMostrar2 += ("<br>El apellido no puede contener caracteres especiales");
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

        //Validar Fecha nacimiento
        const tiempoTranscurrido = Date.now();
        const fechaActual = new Date(tiempoTranscurrido);
        var edadMinima = 18;


        
        if(fechaNacimiento === ''){
            msjMostrar4 += ("Selecciona tu fecha de nacimiento");
            enviarfech = true;
            return
        }
        
        var diferencia = fechaActual - fechaNacimiento;
        var edad = Math.floor(diferencia / (1000 * 60 * 60 * 24 * 365.25));

        if (edad < edadMinima) {
            msjMostrar4 += ("Debes ser mayor de 18 años");
            enviarfech = true;
        }

        if (enviarfech) {
                $("#incompleto4").css("color", "red");
                $("#incompleto4").html(msjMostrar4);
    
            }
        else {
                $("#incompleto4").css("color", "green");
                $("#incompleto4").html("Completado");
            }
            


        //Validacion de email
        var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (correo === '') {
            msjMostrar6 += ("Por favor, ingrese su correo ");
            enviarcorreo = true;
        }
        if (!regex.test(correo)) {
            msjMostrar6 += ("<br>Su correo es invalido");
            enviarcorreo = true;
        }
        if (enviarcorreo) {
            $("#incompleto6").css("color", "red");
            $("#incompleto6").html(msjMostrar6);

        }
        else {
            $("#incompleto6").css("color", "green");
            $("#incompleto6").html("Completado");
        }

        //Validar Contraseña

        var password = $("#clave").val();
        var mayuscula = /[A-Z]/.test(password);
        var minuscula = /[a-z]/.test(password);
        var numero = /[0-9]/.test(password);
        var caracter = /[!@#$%^&*(),.?":{}|<>]/;

        
        if (password === ''){
            msjMostrar3 += ("Por favor, ingresa tu contraseña");
            enviarclav = true;
        }
        if (!caracter.test(password)) {
            msjMostrar3 += ("<br>La contraseña debe contener al menos un caracter especial");
            enviarclav = true;
        }

        if (!mayuscula) {
            msjMostrar3 += ("<br>La contraseña debe contener al menos una letra mayúscula.");
            enviarclav = true;
        }

        if (!minuscula) {
            msjMostrar3 += ("<br>La contraseña debe contener al menos una letra minúscula.");
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
        
        // Validar confirmar contraseña y email
        var confirmPassword = $('#confclave').val();
        
        if (password !== confirmPassword) {
            msjMostrar7 += ("El email no coincide");
            enviarconfcorreo = true;
        }
        if (enviarconfcorreo) {
            $("#incompleto7").css("color", "red");
            $("#incompleto7").html(msjMostrar7);

        }
        else {
            $("#incompleto7").css("color", "green");
            $("#incompleto7").html("Completado");
        }

        var confirmPassword = $('#confclave').val();
        
        if (password !== confirmPassword) {
            msjMostrar8 += ("La contraseña no coincide");
            enviarconfclave = true;
        }
        if (enviarconfclave) {
            $("#incompleto8").css("color", "red");
            $("#incompleto8").html(msjMostrar8);

        }
        else {
            $("#incompleto8").css("color", "green");
            $("#incompleto8").html("Completado");
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