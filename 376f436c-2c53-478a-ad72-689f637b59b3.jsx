// Create a reference to the photo
var photo = new File("C:\\Users\\kalis\\Capstone2023-changes\\uploads\\grace.jpg");

// Check if the photo exists
if (photo.exists) {

    // Open the photo
    var doc = app.open(photo);

    // Create a new layer
    var blurLayer = doc.artLayers.add();

    // Set the layer to the Gaussian Blur filter
    blurLayer.applyGaussianBlur(10);
}
else {
    alert("Photo does not exist!");
}