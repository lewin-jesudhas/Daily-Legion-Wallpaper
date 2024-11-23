import os
import ctypes
import time
import subprocess

# Path to the wallpaper generator script
WALLPAPER_GENERATOR_SCRIPT = "wallpaper_generator.py"

# Path to the downloaded image
DOWNLOADED_IMAGE = os.path.join(os.getcwd(), "downloaded_image.jpg")


def set_wallpaper(image_path):
    """
    Set the desktop wallpaper to the specified image.
    This works for Windows.
    """
    try:
        # Use ctypes to set the wallpaper
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
        print(f"Wallpaper updated to {image_path}")
    except Exception as e:
        print(f"Failed to set wallpaper: {e}")


def download_and_update_wallpaper():
    """
    Run the wallpaper generator script and update the wallpaper.
    """
    try:
        # Run the wallpaper generator script
        subprocess.run(["python", WALLPAPER_GENERATOR_SCRIPT], check=True)
        print("Wallpaper generated successfully.")

        # Set the wallpaper to the newly downloaded image
        set_wallpaper(DOWNLOADED_IMAGE)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    while True:
        download_and_update_wallpaper()
        print("Waiting for 15 minutes...")
        time.sleep(15 * 60)  
