from PIL import Image
import os

# Folder containing PNG images
folder = "GIF_input"  # change this to your folder path

# Get all PNG files
png_files = [f for f in os.listdir(folder) if f.endswith(".png")]

# Sort files numerically
png_files.sort(key=lambda x: int(os.path.splitext(x)[0]))

# Open images
images = [Image.open(os.path.join(folder, f)) for f in png_files]

# Save as GIF
images[0].save(
    "output.gif",
    save_all=True,
    append_images=images[1:],
    duration=200,  # milliseconds per frame
    loop=0         # loop forever
)

print("GIF created successfully as output.gif")
