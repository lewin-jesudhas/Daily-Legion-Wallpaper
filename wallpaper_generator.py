from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
import random

# Configuration
WEBSITE_URL = "https://gaming.lenovo.com/wallpapers"

# Initialize WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    driver.get(WEBSITE_URL)
    time.sleep(10)  # Wait for the page to load completely

    # Handle "Reject all optional cookies" button
    try:
        reject_button = driver.find_element(By.ID, "_evidon-barrier-declinebutton")
        print("Reject cookies button found, clicking it...")
        reject_button.click()
        time.sleep(2)  # Allow time for the button action to take effect
    except Exception as e:
        print("No 'Reject all optional cookies' button detected, proceeding.")

    # Find all image divs
    image_divs = driver.find_elements(By.CLASS_NAME, "w-full.h-full.bg-cover")  # Adjust the class name if necessary

    if image_divs:
        selected_image = random.choice(image_divs)
        actions = ActionChains(driver)
        actions.move_to_element(selected_image).perform()
        time.sleep(1)  # Allow the page to stabilize
        selected_image.click()
        print("Image div selected and clicked.")
        time.sleep(15)  # Wait for the image details page to load

        # Locate the image tag and extract the 'src' attribute
        image_tag = driver.find_element(By.CSS_SELECTOR, "img.cursor-pointer.rounded-base")
        image_src = image_tag.get_attribute("src")
        print(f"Image source URL: {image_src}")
        image_name = "downloaded_image.jpg"  
        response = requests.get(image_src)
        if response.status_code == 200:
            with open(image_name, "wb") as file:
                file.write(response.content)
            print(f"Image downloaded and saved as {image_name}")
        else:
            print("Failed to download the image.")

    else:
        print("No images found with the specified class.")

finally:
    driver.quit()