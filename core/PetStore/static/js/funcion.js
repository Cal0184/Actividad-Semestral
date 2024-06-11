
function validarFormulario(event) {
    event.preventDefault();
    var formulario = document.getElementById('formRegistro');
    var inputs = formulario.getElementsByTagName('input');
    var select = formulario.getElementsByTagName('select')[0];
    var valido = true;

    // Limpiar mensajes de error previos
    var mensajesError = document.getElementsByClassName('error-message');
    while (mensajesError.length > 0) {
        mensajesError[0].parentNode.removeChild(mensajesError[0]);
    }

    // Validar campos de texto
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].type !== 'submit' && inputs[i].value.trim() === '') {
            inputs[i].classList.add('error');
            var mensaje = document.createElement('div');
            mensaje.className = 'error-message';
            mensaje.innerText = 'Este campo es obligatorio';
            inputs[i].parentNode.insertBefore(mensaje, inputs[i].nextSibling);
            valido = false;
        } else {
            inputs[i].classList.remove('error');
        }
    }

    // Validar selección de región
    if (select.value === '') {
        select.classList.add('error');
        var mensaje = document.createElement('div');
        mensaje.className = 'error-message';
        mensaje.innerText = 'Este campo es obligatorio';
        select.parentNode.insertBefore(mensaje, select.nextSibling);
        valido = false;
    } else {
        select.classList.remove('error');
    }

    // Validar que las contraseñas coincidan
    var _pass = formulario.querySelector('input[name="_pass"]');
    var confirmarPass = formulario.querySelector('input[name="confirmar_pass"]');
    if (_pass.value !== confirmarPass.value) {
        _pass.classList.add('error');
        confirmarPass.classList.add('error');
        var mensaje = document.createElement('div');
        mensaje.className = 'error-message';
        mensaje.innerText = 'Las contraseñas no coinciden';
        confirmarPass.parentNode.insertBefore(mensaje, confirmarPass.nextSibling);
        valido = false;
    }

    // Validar longitud de contraseña y número
    if (_pass.value.length < 8 || !/\d/.test(_pass.value)) {
        _pass.classList.add('error');
        var mensaje = document.createElement('div');
        mensaje.className = 'error-message';
        mensaje.innerText = 'La contraseña debe tener al menos 8 caracteres y contener al menos un número';
        _pass.parentNode.insertBefore(mensaje, _pass.nextSibling);
        valido = false;
    }

    if (valido) {
        formulario.submit();
    }
}




function cambiarMascotas(){
    const selectElement = document.getElementById('viewSelector');
        if (selectElement.value) {      
            window.location.href = selectElement.value;
        }
}

function cambiarProductos(){
    const selectElement = document.getElementById('viewSelector1');
        if (selectElement.value) {      
            window.location.href = selectElement.value;
        }
}

