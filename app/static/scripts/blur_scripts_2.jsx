if (app.documents.length > 0) {
    var doc = app.activeDocument;
    var blurRadius = 10; // Set the blur radius in pixels
    var blurLayer = doc.artLayers.add();
    blurLayer.blendMode = BlendMode.NORMAL;
    doc.activeLayer.copy();
    doc.activeLayer = blurLayer;
    doc.paste();
    blurLayer.applyAverage();
    blurLayer.opacity = 50; // You can adjust opacity to control the intensity of the blur
}

