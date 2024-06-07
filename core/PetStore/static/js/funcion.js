document.getElementById('formularioReg').addEventListener('submit', function(event) {
    event.preventDefault();

    var nombre = document.getElementById('nombre').value;
    var ape = document.getElementById('ape').value;
    var email = document.getElementById('email').value;
    var pass1 = document.getElementById('pass1').value;
    var pass2 = document.getElementById('pass2').value;
    var direccion = document.getElementById('direccion').value;
    var region = document.getElementById('region').value;
    var zip = document.getElementById('zip').velue;
    
    
    if (nombre === "" || ape === "" || email === "" || pass1 === "" || pass2 === "" || direccion === "" || zip === "" || region === "0"){
        alert("Por favor, completa todos los campos.");
    }else if (!validateEmail(email)){
        alert("Por favor, ingresa un correo con formato válido.");
    }else if (pass1!= pass2){
        alert("Las contraseñas no coinciden.");
    }else if (!validatePass(pass1)){
        alert("La contraseña debe tener al menos 8 caracteres, incluyendo letras, números y al menos un carácter especial.");
    } else if (region === "0"){
        alert("Debe seleccionar una región.");
    } else if (!validateZip){
        alert("El formato del Código postal no coincide.")
    }else {
        console.log('Nombre:', nombre, 'Apellidos:', ape, 'Email:', email, 'Contraseña:', pass1, 'Dirección:', direccion, 'Zip:', zip, 'Region:',region);
    }
});

function validateEmail(email) {
    var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

function validatePass(pass1) {
    var regex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return regex.test(pass1);
}

function validateZip(zip) {
    var regex = /^\d{8}$/;
    return regex.test(zip);
}

function cambiarMascotas(){
    const selectElement = document.getElementById('viewSelector');
        if (selectElement.value) {      
            window.location.href = selectElement.value;
        }
}

document.addEventListener('DOMContentLoaded', (event) => {
    const selectElement = document.getElementById('viewSelector');
    selectElement.addEventListener('change', (event) => {
        const selectedValue = event.target.value;
        if (selectedValue) {
            window.location.href = selectedValue;
        }
    });
});

document.addEventListener('DOMContentLoaded', (event) => {
    const selectElement = document.getElementById('viewSelector1');

    selectElement.addEventListener('change', (event) => {
        const selectedValue = event.target.value;
        if (selectedValue) {
            window.location.href = selectedValue;
        }
    });
});