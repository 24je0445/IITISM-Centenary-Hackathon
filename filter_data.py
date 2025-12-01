import os
import shutil

# --- SMART CONFIGURATION ---
# We will search the ENTRIE project folder for images
PROJECT_ROOT = r"C:\Users\rajru\Desktop\Hackathon_Project"
DEST_FOLDER = r"C:\Users\rajru\Desktop\Hackathon_Project\filtered_images"

# Image types to look for
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.avif', '.gif')

# Create destination folder
if not os.path.exists(DEST_FOLDER):
    os.makedirs(DEST_FOLDER)

print(f"🚀 Starting Deep Search in: {PROJECT_ROOT}")

count = 0
found_paths = []

# 1. Walk through EVERY folder in your project
for root, dirs, files in os.walk(PROJECT_ROOT):
    
    # Skip the destination folder itself (so we don't copy copies)
    if "filtered_images" in root:
        continue

    for file in files:
        # Check if it is an image
        if file.lower().endswith(IMAGE_EXTENSIONS):
            file_path = os.path.join(root, file)
            
            try:
                # Check size (Lowered limit to 10KB to be safe)
                file_size_kb = os.path.getsize(file_path) / 1024
                
                if file_size_kb > 10:  # Keep anything bigger than 10KB
                    # Handle duplicate filenames by adding a number
                    new_filename = file
                    if os.path.exists(os.path.join(DEST_FOLDER, new_filename)):
                        base, ext = os.path.splitext(file)
                        new_filename = f"{base}_{count}{ext}"

                    # Copy it
                    shutil.copy(file_path, os.path.join(DEST_FOLDER, new_filename))
                    print(f"✅ Found & Saved: {new_filename} (from {root})")
                    count += 1
                    
            except Exception as e:
                print(f"❌ Error reading {file}: {e}")

print("-" * 30)
if count == 0:
    print("⚠️ WARNING: No images found! Are you sure you UNZIPPED the dataset files?")
else:
    print(f"🎉 SUCCESS! Found and copied {count} images to 'filtered_images' folder.")
