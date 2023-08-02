// Create a new document and specify a width and height
var doc = app.documents.add(500, 500);

// Load the image into the document
var fileRef = File("C:/Users/kalis/Capstone2023-changes/uploads/house1.jpg");
doc.placedItems.add(fileRef);

// Apply a Gaussian Blur effect to the image
doc.activeLayer.applyGaussianBlur(10);