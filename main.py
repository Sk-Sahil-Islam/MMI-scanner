from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# To make browser window automatically open, comments these 3 lines below (line 8,9,10)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

print("Web Scraper is running...")

print("Loading the CNN Fear and Greed Index page...")
driver.get("https://edition.cnn.com/markets/fear-and-greed")
print(" ")

time.sleep(5)

try:
    mmi_result = driver.find_element(By.CLASS_NAME, "market-fng-gauge__historical-item-index-value")
    mmi = int(mmi_result.text)
    print(f"Market Mood Index (MMI) Score: {mmi}")
except Exception as e:
    print(f"An error occurred: {e}")

if (0 <= mmi <= 24):
    print("Sentiment: Extreme Fear")
elif (25 <= mmi <= 44):
    print("Sentiment: Fear")
elif (44 < mmi <= 55):
    print("Sentiment: Neutral")
elif (55 < mmi <= 75):
    print("Sentiment: Greed")
elif (76 < mmi <= 100):
    print("Sentiment: Extreme Greed")

driver.quit()
print("Program finished.")
