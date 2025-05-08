#!/usr/bin/env python3

from PIL import Image
import os

# Corrected path handling
input_folder = os.path.expanduser("~/helloWorld/images")
output_folder = os.path.expanduser("/opt/icons")

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

# Process images
for file_name in os.listdir(input_folder):
    if file_name.endswith(".tiff"):
        img_path = os.path.join(input_folder, file_name)
        img = Image.open(img_path)

        # Rotate, resize, and convert format
        img = img.rotate(-90).resize((128, 128))
        output_path = os.path.join(output_folder, file_name.replace(".tiff", ".jpeg"))
        img.convert("RGB").save(output_path, "JPEG")

print("Image processing complete!")
print(f"Processed images saved to: {output_folder}")
