// blur photo
// This code requires Adobe Photoshop CS6 or later

// Declare variables
var photoPath = "C:\\Users\\kalis\\Capstone2023-shortcuts\\uploads\\BlackPanther.jpg";
var editedPhotoPath = "C:\\Users\\kalis\\Capstone2023-shortcuts\\editedphotos\\BlackPanther.jpg";

// Open the photo
var doc = app.open(File(photoPath));

// Apply blur filter
doc.activeLayer.applyGaussianBlur(5.0);

// Save the edited photo
var saveOptions = new JPEGSaveOptions();
doc.saveAs(File(editedPhotoPath), saveOptions, true);

// Close the photo
doc.close(SaveOptions.DONOTSAVECHANGES);