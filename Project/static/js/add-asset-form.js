function updateForm() {
    const assetType = document.getElementById('id_type_of_asset').value;
    const hardwareType = document.getElementById('id_hardware_type').value;

    const hardwareTypeField = document.getElementById('hardware_type_group');
    const detailedHardwareFields = document.getElementById('detailed_hardware_fields');
    const brandModelFields = document.getElementById('brand_model_fields');
    const genericBrandModelFields = document.getElementById('generic_brand_model_fields');

    // Show or hide fields based on asset type
    if (assetType === 'hardware') {
        hardwareTypeField.style.display = 'block';

        if (hardwareType === 'computer') {
            detailedHardwareFields.style.display = 'block';
            brandModelFields.style.display = 'block';
            genericBrandModelFields.style.display = 'none';
        } else if (hardwareType) {
            detailedHardwareFields.style.display = 'none';
            brandModelFields.style.display = 'block';
            genericBrandModelFields.style.display = 'none';
        } else {
            detailedHardwareFields.style.display = 'none';
            brandModelFields.style.display = 'none';
            genericBrandModelFields.style.display = 'none';
        }
    } else {
        hardwareTypeField.style.display = 'none';
        detailedHardwareFields.style.display = 'none';
        brandModelFields.style.display = 'none';
        genericBrandModelFields.style.display = 'block';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('id_type_of_asset').addEventListener('change', updateForm);
    document.getElementById('id_hardware_type').addEventListener('change', updateForm);
    updateForm(); // Initialize form state
});
