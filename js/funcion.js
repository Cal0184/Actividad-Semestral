document.getElementById('miFormulario').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que el formulario se envíe de forma predeterminada
    var nombre = document.getElementById('nombre').value; // Captura el valor del campo de nombre
    var email = document.getElementById('email').value; // Captura el valor del campo de email
    console.log('Nombre:', nombre, 'Email:', email); // Muestra los datos en la consola
});
