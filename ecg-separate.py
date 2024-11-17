import os
from PIL import Image

# Define the input and output directories
input_dir = "ecg_plots_images"  # Folder containing the ECG images
output_dir = "output_images"  # Folder to save the split images

# Function to split and save image
def split_and_save_image(image_path, output_path):
    with Image.open(image_path) as img:
        # Define the coordinates for cropping the left half
        left_half_box = (0, 0, 2103, 1377)  # (left, upper, right, lower)

        # Crop the left half of the image
        left_half = img.crop(left_half_box)

        # Define the coordinates for cropping the right half
        right_half_box = (2103, 0, img.width, 1377)  # (left, upper, right, lower)

        # Crop the right half of the image
        right_half = img.crop(right_half_box)

    # Save the left and right halves as separate images
    left_output_path = output_path.format("left")
    right_output_path = output_path.format("right")
    left_half.save(left_output_path)
    right_half.save(right_output_path)
    print(f"Split and saved {image_path} into {left_output_path} and {right_output_path}")

# Process each image in the input directory
for i, filename in enumerate(os.listdir(input_dir)):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Filter only image files
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, "ecg_plot_{}_{}.jpg".format(i + 1, "{}"))
        split_and_save_image(input_path, output_path)
