from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize_driver():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def main():
    driver = initialize_driver()
    url = "https://www.flipkart.com/"
    # url = "https://www.amazon.in/"
    driver.get(url)
    # submit_button = driver.find_element(By.XPATH , "//input[@type='submit']")
    # submit_button = driver.find_element(By.ID , "nav-search-submit-button")

    try:
        # submit_button = WebDriverWait(driver, 30).until(
        #     EC.presence_of_element_located((By.XPATH, "//input[@type='submit']"))
        # )

        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_2KpZ6l _2doB4z"))
        )
        submit_button.click()

    finally:
        driver.quit()

if __name__ == '__main__':
    main()