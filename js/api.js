//API REGIONES, COMUNAS

function miFuncionCallbackRegiones(data) {
    let cad = '';
    for (let i = 0; i < data.length; i++) {
        const region = data[i];
        cad += <option value="${region.codigo}">${region.nombre}</option>;
    }
    document.getElementById("region").innerHTML = <option value="">Seleccione una Región</option> + cad;
}

const urlJSONPRegiones = 'https://apis.digital.gob.cl/dpa/regiones/?callback=miFuncionCallbackRegiones';
const scriptRegiones = document.createElement('script');
scriptRegiones.src = urlJSONPRegiones;
document.body.appendChild(scriptRegiones);

function obtenerComunas() {
    const regionSeleccionada = document.getElementById("region").value;
    if (regionSeleccionada !== "") {
        const urlJSONPComunas = https//apis.digital.gob.cl/dpa/regiones/${regionSeleccionada}/comunas/?callback=miFuncionCallbackComunas;
        const scriptComunas = document.createElement('script');
        scriptComunas.src = urlJSONPComunas;
        document.body.appendChild(scriptComunas);
    } else {
        limpiarComunas();
    }
}

function limpiarComunas() {
    document.getElementById("comuna").innerHTML = "<option value=''>Seleccione una Comuna</option>";
}

function miFuncionCallbackComunas(data) {
    let cad = '';
    for (let i = 0; i < data.length; i++) {
        const comuna = data[i];
        cad += <option value="${comuna.codigo}">${comuna.nombre}</option>;
    }
    document.getElementById("comuna").innerHTML = <option value="">Seleccione una Comuna</option> + cad;
}