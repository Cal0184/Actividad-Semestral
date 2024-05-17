document.addEventListener('DOMContentLoaded', (event) => {
    const selectElement = document.getElementById('viewSelector');

    selectElement.addEventListener('change', (event) => {
        const selectedValue = event.target.value;
        if (selectedValue) {
            window.location.href = selectedValue;
        }
    });
});
