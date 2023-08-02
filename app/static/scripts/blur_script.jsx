// Check if a document is open
if (app.documents.length > 0) {
  // Get the active document
  var doc = app.activeDocument;

  // Set the amount of Gaussian Blur (radius in pixels)
  var blurAmount = 10;

  // Create a new Blur Gallery filter
  var blurFilter = new BlurFilter(blurAmount);
  var blurGallery = blurGalleryFilter.galleryOptions;

  // Set the blur amount
  blurGallery.blur = blurAmount;
  }

  // Apply the filte
  blurGallery.applyFilter(blurFilter);