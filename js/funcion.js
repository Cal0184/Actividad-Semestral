document.getElementById('formularioReg').addEventListener('submit', function(event) {
    event.preventDefault();
    var nombre = document.getElementById('nombre').value; 
    var email = document.getElementById('email').value; 
    console.log('Nombre:', nombre, 'Email:', email); 
});
