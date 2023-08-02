// Check if a document is open
if (app.documents.length > 0) {
  // Get the active document
  var doc = app.activeDocument;

  // Set the crop bounds (in pixels)
  var left = 100;    // Left edge of the crop rectangle
  var top = 100;     // Top edge of the crop rectangle
  var right = 300;   // Right edge of the crop rectangle
  var bottom = 300;  // Bottom edge of the crop rectangle

  // Set the ruler units to pixels (Photoshop CS6)
  app.preferences.rulerUnits = Units.PIXELS;

  // Apply the crop directly
  doc.crop([left, top, right, bottom]);

  // Save the changes
  //doc.save();
} else {
  alert("No document is open in Photoshop.");
}
