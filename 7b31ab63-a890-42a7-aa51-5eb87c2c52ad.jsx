// Blur Photo
// The path to photo is C:\Users\kalis\Capstone2023-changes\uploads\annie.jpg

// Create a new file object
var file = new File("C:\Users\kalis\Capstone2023-changes\uploads\annie.jpg");

// Open the file
file.open("r");

// Create a new image object
var img = new Image(file);

// Blur the image
img.blur(10);

// Close the file
file.close();