from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

WEBSITE_URL = "https://gaming.lenovo.com/wallpapers"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    driver.get(WEBSITE_URL)
    time.sleep(15)  

    # Handle cookie consent or overlay (if present)
    try:
        overlay = driver.find_element(By.ID, "_evidon-background")
        print("Overlay found, dismissing it...")
        overlay.click()
        time.sleep(2)  # Allow time for the overlay to disappear
    except Exception as e:
        print("No overlay detected, proceeding.")

    # Find all image divs
    image_divs = driver.find_elements(By.CLASS_NAME, "w-full.h-full.bg-cover")  # Adjust the class name if necessary

    # Select the first image (or a random one)
    if image_divs:
        #selected_image = image_divs[0]  # Automatically pick the first image
        # To select a random image:
        import random
        selected_image = random.choice(image_divs)
        actions = ActionChains(driver)
        actions.move_to_element(selected_image).perform()
        time.sleep(1)  # Allow the page to stabilize
        selected_image.click()
        print("Image selected and clicked.")
        time.sleep(15)  # Wait for the wallpaper details page to load

        # Click the "Download 4K" button
        download_4k_xpath = "/html/body/div[1]/div/div[1]/div/main/div/div/div[2]/div[2]/div/div/div/div[1]/a"
        download_button = driver.find_element(By.XPATH, download_4k_xpath)
        
        # Scroll into view and click the download button
        actions.move_to_element(download_button).perform()
        download_button.click()
        print("Download initiated.")
        time.sleep(10)  # Wait for the download to complete
    else:
        print("No images found with the specified class.")

finally:
    driver.quit()
