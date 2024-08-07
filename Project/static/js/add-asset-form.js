document.addEventListener('DOMContentLoaded', function() {
    const typeOfAssetSelect = document.getElementById('id_type_of_asset');
    const hardwareTypeContainer = document.getElementById('hardware_type_container');
    const hardwareFields = document.getElementById('hardware_fields');
    const hardwareTypeSelect = document.getElementById('id_hardware_type');
    const allDynamicFields = document.querySelectorAll('.dynamic-fields');

    // Show/hide hardware type container based on asset type selection
    typeOfAssetSelect.addEventListener('change', function() {
        const selectedType = this.value;
        if (selectedType === 'hardware') {
            hardwareTypeContainer.style.display = 'block';
        } else {
            hardwareTypeContainer.style.display = 'none';
            hardwareFields.style.display = 'none'; // Hide all hardware fields
        }

        // Hide all other dynamic fields
        allDynamicFields.forEach(field => field.style.display = 'none');
    });

    // Show/hide specific hardware fields based on hardware type selection
    hardwareTypeSelect.addEventListener('change', function() {
        const selectedHardwareType = this.value;
        hardwareFields.style.display = selectedHardwareType ? 'block' : 'none';
        
        // Hide all specific hardware fields
        allDynamicFields.forEach(field => field.style.display = 'none');

        // Show fields for the selected hardware type
        const selectedFields = document.getElementById(selectedHardwareType + '_fields');
        if (selectedFields) {
            selectedFields.style.display = 'block';
        }
    });
});
