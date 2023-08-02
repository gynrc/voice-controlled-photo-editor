// Create a new Photoshop document
var doc = app.documents.add(1000, 1000);

// Open the photo
var fileRef = File( "C:/Users/kalis/Capstone2023-changes/uploads/endgame.jpg" );
doc.artLayers.add()
doc.activeLayer.file = fileRef;

// Blur the photo
var blurFilter = doc.activeLayer.applyGaussianBlur( 5 );