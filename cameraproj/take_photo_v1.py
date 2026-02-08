from picamera2 import Picamera2
from datetime import datetime
import time

picam2 = Picamera2()

# Configure for still capture
config = picam2.create_still_configuration()
picam2.configure(config)

# 🔍 ZOOM SETTINGS (adjust these)
# Full sensor is typically 4608x2592 on v2 camera
sensor_width = 4608
sensor_height = 2592

zoom_factor = 1.2  # 1.0 = no zoom, 2.0 = strong zoom

crop_width = int(sensor_width / zoom_factor)
crop_height = int(sensor_height / zoom_factor)

crop_x = (sensor_width - crop_width) // 2
crop_y = (sensor_height - crop_height) // 2

picam2.set_controls({
    "ScalerCrop": (crop_x, crop_y, crop_width, crop_height)
})

picam2.start()
time.sleep(2)

print("Camera ready (zoom factor:", zoom_factor, ")")
print("Press Enter to take a picture.")
print("Type 'q' and press Enter to quit.")

while True:
    key = input()

    if key.strip().lower() == "q":
        print("Exiting...")
        break

    filename = datetime.now().strftime("photo_%Y%m%d_%H%M%S.png")
    picam2.capture_file(filename)
    print(f"Photo saved as {filename}")

picam2.stop()



