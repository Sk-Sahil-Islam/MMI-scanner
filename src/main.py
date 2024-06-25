from appwrite.client import Client
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time
import os

def main(context):

    # You can log messages to the console
    context.log("Hello, Logs!")

    # If something goes wrong, log an error
    context.error("Hello, Errors!")

    # The `ctx.req` object contains the request data
    if context.req.method == "GET":
        # Send a response with the res object helpers
        # `ctx.res.send()` dispatches a string back to the client
        return context.res.send("Hello, World!")

    # `ctx.res.json()` is a handy helper for sending JSON
    mmi = getMmi()
    return context.res.json(
        {
            "mmi": mmi
        }
    )
def getMmi():
    # Initialize Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    # Initialize the WebDriver
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    # Visit the target webpage
    driver.get("https://edition.cnn.com/markets/fear-and-greed")

    # Wait for the page to load
    time.sleep(5)

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

    # Create the JSON response
    response = json.dumps({ "mmi": mmi })
    return response