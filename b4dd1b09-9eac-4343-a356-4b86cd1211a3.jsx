// blur photo
// create a reference to the file
var fileRef = new File("C:\\Users\\kalis\\Capstone2023-changes\\uploads\\annie.jpg");
// open the file
fileRef.open("r");
// read the file
var img = fileRef.read();
// create a new document
app.documents.add();
// place the image
app.activeDocument.placedItems.add().file = fileRef;
// close the file
fileRef.close();
// apply the blur filter
app.activeDocument.activeLayer.applyGaussianBlur(5);