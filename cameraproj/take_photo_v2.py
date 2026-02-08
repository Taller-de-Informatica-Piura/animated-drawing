
from picamera2 import Picamera2, Preview
from datetime import datetime
import time
import sys
import termios
import tty

# -----------------------------
# KEYBOARD INPUT
# -----------------------------
def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch1 = sys.stdin.read(1)

        if ch1 == "\x1b":  # Escape sequence
            ch2 = sys.stdin.read(1)
            ch3 = sys.stdin.read(1)
            return ch1 + ch2 + ch3

        return ch1

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


# -----------------------------
# CAMERA SETUP
# -----------------------------
picam2 = Picamera2()

config = picam2.create_preview_configuration()
picam2.configure(config)

picam2.start_preview(Preview.QTGL)
picam2.start()

time.sleep(2)

sensor_width = 4608
sensor_height = 2592

zoom_factor = 1.0

crop_width = sensor_width
crop_height = sensor_height
crop_x = 0
crop_y = 0

STEP = 200


def apply_crop():
    picam2.set_controls({
        "ScalerCrop": (
            int(crop_x),
            int(crop_y),
            int(crop_width),
            int(crop_height),
        )
    })


print("\nControls:")
print(" Arrows / WASD / Numpad 2-4-6-8 → Move")
print(" + / - → Zoom")
print(" ENTER → Photo")
print(" q → Quit\n")

# -----------------------------
# LOOP
# -----------------------------
while True:
    key = get_key()

    # Quit
    if key == "q":
        break

    # Photo
    elif key in ["\r", "\n"]:
        filename = datetime.now().strftime("photo_%Y%m%d_%H%M%S.png")
        picam2.capture_file(filename)
        print("Saved:", filename)

    # -------- ZOOM --------
    elif key == "+":
        zoom_factor = min(zoom_factor + 0.1, 3.0)

    elif key == "-":
        zoom_factor = max(1.0, zoom_factor - 0.1)

    crop_width = sensor_width / zoom_factor
    crop_height = sensor_height / zoom_factor

    # -------- PAN --------
    # Left
    if key in ["\x1b[D", "\x1bOD", "a", "4"]:
        crop_x -= STEP

    # Right
    elif key in ["\x1b[C", "\x1bOC", "d", "6"]:
        crop_x += STEP

    # Up
    elif key in ["\x1b[A", "\x1bOA", "w", "8"]:
        crop_y -= STEP

    # Down
    elif key in ["\x1b[B", "\x1bOB", "s", "2"]:
        crop_y += STEP

    # Clamp
    crop_x = min(max(0, crop_x), sensor_width - crop_width)
    crop_y = min(max(0, crop_y), sensor_height - crop_height)

    apply_crop()

picam2.stop_preview()
picam2.stop()

