document.addEventListener('DOMContentLoaded', function () {
    var currentMethodSelect = document.getElementById('current_method');
    var colorContainer = document.getElementById('valueContainer');
    var colorContainer = document.getElementById('colorContainer');
    var indexContainer = document.getElementById('indexContainer');

    currentMethodSelect.addEventListener('change', function () {
        var selectedOperation = this.value;

        // Show/hide  value input based on selected operation
        if (['shift', 'pop', 'remove', 'reverse'].includes(selectedOperation)) {
            valueContainer.classList.add('hidden');
        } else {
            valueContainer.classList.remove('hidden');
        }
        
        // Show/hide color input based on selected operation
        if (['shift', 'pop', 'remove', 'reverse'].includes(selectedOperation)) {
            colorContainer.classList.add('hidden');
        } else {
            colorContainer.classList.remove('hidden');
        }

        // Show/hide index input based on selected operation
        if (selectedOperation === 'set' || selectedOperation === 'insert' || selectedOperation === 'remove') {
            indexContainer.classList.remove('hidden');
        } else {
            indexContainer.classList.add('hidden');
        }
    });
});
