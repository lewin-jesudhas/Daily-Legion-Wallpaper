# import os
# import requests
# from bs4 import BeautifulSoup
# from PIL import Image
# import ctypes
# import schedule
# import time

# # Directory to store wallpapers
# WALLPAPER_DIR = os.path.expanduser("~\\Wallpapers")
# if not os.path.exists(WALLPAPER_DIR):
#     os.makedirs(WALLPAPER_DIR)

# # File to track downloaded wallpapers
# TRACK_FILE = os.path.join(WALLPAPER_DIR, "downloaded_wallpapers.txt")
# if not os.path.exists(TRACK_FILE):
#     open(TRACK_FILE, "w").close()

# # Lenovo wallpaper website URL
# BASE_URL = "https://gaming.lenovo.com/wallpapers"

# def fetch_wallpapers():
#     """Fetch wallpaper URLs from the Lenovo website."""
#     response = requests.get(BASE_URL)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     wallpapers = soup.find_all('img', class_="wallpaper-class")  
#     return [wallpaper['src'] for wallpaper in wallpapers if 'src' in wallpaper.attrs]

# def download_wallpaper(url):
#     """Download a wallpaper from the given URL."""
#     response = requests.get(url, stream=True)
#     if response.status_code == 200:
#         filename = os.path.join(WALLPAPER_DIR, url.split('/')[-1])
#         with open(filename, 'wb') as f:
#             f.write(response.content)
#         return filename
#     return None

# def set_wallpaper(image_path):
#     """Set the downloaded image as the desktop wallpaper."""
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

# def update_wallpaper():
#     """Main function to update the wallpaper daily."""
#     print("Fetching wallpapers...")
#     wallpaper_urls = fetch_wallpapers()

#     with open(TRACK_FILE, "r") as f:
#         downloaded = f.read().splitlines()

#     new_wallpapers = [url for url in wallpaper_urls if url not in downloaded]
#     if not new_wallpapers:
#         print("No new wallpapers available.")
#         return

#     new_wallpaper_url = new_wallpapers[0] 
#     print(f"Downloading wallpaper: {new_wallpaper_url}")
#     wallpaper_path = download_wallpaper(new_wallpaper_url)

#     if wallpaper_path:
#         print("Setting wallpaper...")
#         set_wallpaper(wallpaper_path)

#         # Update the track file
#         with open(TRACK_FILE, "a") as f:
#             f.write(new_wallpaper_url + "\n")
#         print("Wallpaper updated successfully!")

# schedule.every().day.at("18:00").do(update_wallpaper)

# print("Wallpaper automation running... Press Ctrl+C to stop.")
# while True:
#     schedule.run_pending()
#     time.sleep(1)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Configuration
WEBSITE_URL = "https://gaming.lenovo.com/wallpapers"

# Initialize WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    # Open the website
    driver.get(WEBSITE_URL)
    time.sleep(15)  # Allow time for the page to load

    # Handle cookie consent or overlay (if present)
    try:
        overlay = driver.find_element(By.ID, "_evidon-background")
        print("Overlay found, dismissing it...")
        overlay.click()
        time.sleep(2)  # Allow time for the overlay to disappear
    except Exception as e:
        print("No overlay detected, proceeding.")

    # Click the first wallpaper on the grid
    first_wallpaper_xpath = "/html/body/div[1]/div/div[1]/div/main/div/div[3]/div[2]/div[2]/ul/div[2]/div[1]/div/div"
    first_wallpaper = driver.find_element(By.XPATH, first_wallpaper_xpath)
    
    # Scroll the wallpaper element into view
    actions = ActionChains(driver)
    actions.move_to_element(first_wallpaper).perform()
    time.sleep(50)  # Allow the page to stabilize
    first_wallpaper.click()
    time.sleep(15)  # Wait for the wallpaper details page to load

    # Click the "Download 4K" button
    download_4k_xpath = "/html/body/div[1]/div/div[1]/div/main/div/div/div[2]/div[2]/div/div/div/div[1]/a"
    download_button = driver.find_element(By.XPATH, download_4k_xpath)
    
    # Scroll into view and click the download button
    actions.move_to_element(download_button).perform()
    download_button.click()
    print("Download initiated.")

    # Wait for the download to complete
    time.sleep(10)

finally:
    driver.quit()
