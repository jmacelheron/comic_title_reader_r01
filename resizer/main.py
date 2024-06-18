from PIL import Image
import os

# Open the image file
image_directory = 'diff/'

for filename in os.listdir(image_directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        image_path = os.path.join(image_directory, filename)
        img = Image.open(image_path)

        # Get the size of the image
        width, height = img.size

        # Calculate the new size
        new_size = (width // 2, height // 2)

        # Resize the image
        img_resized = img.resize(new_size)

        filename = os.path.basename(image_path)
        new_dir = 'minified_images/'
        new_path = os.path.join(new_dir, filename)
        # Save the resized image
        img_resized.save(new_path)