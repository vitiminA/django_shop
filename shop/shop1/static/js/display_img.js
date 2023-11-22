var imageInput = document.getElementById('id_image');
imageInput.setAttribute('onchange', 'previewImage(this)');
function previewImage(input) {
    var preview = document.getElementById('image-preview');
    var file = input.files[0];
    var reader = new FileReader();

    reader.onload = function(e) {
        preview.src = e.target.result;
    };

    if (file) {
        reader.readAsDataURL(file);
    }
}