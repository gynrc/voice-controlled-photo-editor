// Check if Photoshop is running
if (BridgeTalk.appName === "photoshop") {
  // Reference the active document
  var doc = app.activeDocument;

  // Function to change the saturation of an image
  function changeSaturation(doc, saturationValue) {
    // Check if the document is in RGB color mode
    if (doc.mode === DocumentMode.RGB) {
      // Convert the active layer to a Smart Object (non-destructive)
      var activeLayer = doc.activeLayer;
      var smartObject = activeLayer.smartObject;
      if (!smartObject) {
        doc.activeLayer = activeLayer;
        doc.activeLayer = doc.activeLayer.duplicate(doc.layers[doc.layers.length - 1], ElementPlacement.PLACEBEFORE);
        doc.activeLayer.rasterize(RasterizeType.SMARTOBJECT);
      }

      // Apply a Hue/Saturation adjustment layer
      var hueSaturationLayer = doc.artLayers.add();
      hueSaturationLayer.kind = LayerKind.HUESATURATION;
      var hueSaturationProperties = hueSaturationLayer.adjustment;

      // Set the saturation value
      hueSaturationProperties.saturation = saturationValue;

      // Confirm the adjustment
      hueSaturationProperties = dialogModes.NO; // Set the dialog mode to "NO" to suppress the confirmation dialog.
      hueSaturationProperties.confirm();

      // Merge the adjustment layer with the layer below
      hueSaturationLayer.merge();

      // Remove the temporary smart object layer if created
      if (!smartObject) {
        doc.activeLayer.remove();
      }
    } else {
      alert("The image must be in RGB mode for this script to work.");
    }
  }

  // Set the saturation value to 70 (convert to percentage format)
  var saturationValue = 70;

  // Call the function to change saturation
  changeSaturation(doc, saturationValue);
} else {
  alert("Please open an image in Adobe Photoshop CS6 before running this script.");
}

