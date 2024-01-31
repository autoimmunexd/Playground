from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()

# Remove the following line if you don't need to set the binary location explicitly
# options.binary_location = 'path/to/firefox'

driver = webdriver.Firefox(options=options)
driver.get("https://discord.com/login")

# Wait for the page to load (you might need to adjust the wait time)
driver.implicitly_wait(10)

# Locate the username, password, and login elements
username = driver.find_element(By.NAME, 'email')
password = driver.find_element(By.NAME, 'password')
login = driver.find_element(By.XPATH, '//button[@type="submit"]')

# Input your credentials and click login
username.send_keys("mclovin")
password.send_keys("bluedru")
login.click()

# Wait for the login process to complete (you might need to add more waiting or use WebDriverWait)
driver.implicitly_wait(10)

# Quit the driver
driver.quit()