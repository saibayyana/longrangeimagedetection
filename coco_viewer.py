import json
import matplotlib.pyplot as plt
from pycocotools.coco import COCO
from PIL import Image
import os
import time

# Define paths
annotation_file = 'C:/project_directory/annotations/instances_val2017.json'
image_dir = 'C:/project_directory/val2017/'

# Load COCO annotations
coco = COCO(annotation_file)

# Get all image IDs in the validation set
image_ids = coco.getImgIds()

# Create a figure with subplots
num_images = 10
fig, axs = plt.subplots(1, num_images, figsize=(15, 10))  # Adjust the figsize as needed

# Start timing
start_time = time.time()

# Initialize counts for efficiency calculation
total_annotations = 0

# Visualize a few images with annotations
for i, img_id in enumerate(image_ids[:num_images]):  # Show the first `num_images` images
    img_info = coco.loadImgs(img_id)[0]
    img_path = os.path.join(image_dir, img_info['file_name'])

    img = Image.open(img_path)
    axs[i].imshow(img)

    # Get the annotations for the image
    ann_ids = coco.getAnnIds(imgIds=img_id)
    annotations = coco.loadAnns(ann_ids)

    # Count total annotations for efficiency calculation
    total_annotations += len(annotations)

    # Plot bounding boxes
    for ann in annotations:
        bbox = ann['bbox']
        axs[i].add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], edgecolor='red', facecolor='none'))

        # Print the category name
        category = coco.loadCats(ann['category_id'])[0]['name']
        print(f"Category: {category}")

    axs[i].axis('off')  # Hide the axis

plt.tight_layout()  # Adjust the layout
plt.show()  # Show the grid of images

# End timing
end_time = time.time()
execution_time = end_time - start_time

# Calculate efficiency (arbitrary metric)
# Efficiency = (number of images processed / execution time) * (total annotations / num_images)
efficiency = (num_images / execution_time) * (total_annotations / num_images) if num_images > 0 else 0

print(f"Efficiency: {efficiency:.2f} annotations per image per second.")
