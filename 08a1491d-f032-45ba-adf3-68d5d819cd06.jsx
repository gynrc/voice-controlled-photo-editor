// Create a new document
var doc = app.documents.add(); 

// Load the photo
var photo = File("C:/Users/kalis/Capstone2023-changes/uploads/endgame.jpg");
doc.placedItems.add(photo);

// Blur the photo
var blur = doc.activeLayer.blur(5);

// Close the document
doc.close(SaveOptions.DONOTSAVECHANGES);