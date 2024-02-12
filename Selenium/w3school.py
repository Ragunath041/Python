from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Run Chrome in headless mode

# Initialize Chrome driver with options
driver = webdriver.Chrome(executable_path=r"C:\chromedriver", options=chrome_options)

# Maximize the window
driver.maximize_window()

# Open Google
driver.get("https://www.google.com/")

# Find the search box and perform a search for "w3school"
search_box = driver.find_element_by_name("q")
search_box.send_keys("w3school")
search_box.send_keys(Keys.ENTER)

# Wait for a few seconds to see the result
time.sleep(3)

# Close the browser
driver.close()
