from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Optional: run browser headless
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()  # Make sure chromedriver is in PATH

# 1. Open Google
driver.get("https://www.google.com")

# 2. Find the search box and enter a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("marketing agency India")
search_box.send_keys(Keys.RETURN)

# 3. Wait and collect result titles
time.sleep(2)
results = driver.find_elements(By.CSS_SELECTOR, 'h3')

# 4. Print result titles
for i, result in enumerate(results[:10], 1):
    print(f"{i}. {result.text}")

driver.quit()