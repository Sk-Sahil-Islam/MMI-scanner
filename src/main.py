from appwrite.client import Client
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path
import json
import time
import os

def main(context):
    mmi = getMmi2()
    return context.res.json(
        {
            "mmi": mmi
        }
    )
def getMmi2():
    # Initialize Chrome options
    #options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    #options.add_argument("--disable-gpu")

    # Initialize the WebDriver
    #service = Service(excutable_path=os.environ.get("CHROMEDRIVER_PATH"))
    #driver = webdriver.Chrome(service=service, options=options)

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    service = Service(executable_path=binary_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Visit the target webpage
    driver.get("https://edition.cnn.com/markets/fear-and-greed")

    # Wait for the page to load
    time.sleep(3)

    mmi = None
    try:
        # Locate the element containing the MMI value
        mmi_result = driver.find_element(By.CLASS_NAME, "market-fng-gauge__historical-item-index-value")
        mmi = int(mmi_result.text)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Quit the WebDriver
        driver.quit()

    return mmi