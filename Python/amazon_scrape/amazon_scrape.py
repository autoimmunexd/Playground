from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Connect to SQLite database
conn = sqlite3.connect('amazon_data.db')
c = conn.cursor()

# Create tables
c.execute('''
    CREATE TABLE IF NOT EXISTS products
    (id INTEGER PRIMARY KEY, title TEXT, type_and_count TEXT)
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS price_history
    (product_id INTEGER, price TEXT, date TEXT,
    FOREIGN KEY(product_id) REFERENCES products(id))
''')

def slow_scroll_to_bottom(driver, scroll_pause_time=0.5):
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scrape_amazon(search_term):
    # Initialize Selenium WebDriver
    driver = webdriver.Chrome()

    # Navigate to Amazon homepage
    driver.get('https://www.amazon.com')

    try:
        # Wait for the search box to become available
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
        )

        # Enter the search term and submit the form
        search_box.send_keys(search_term)
        search_box.submit()
        time.sleep(2)  # Wait for the page to load

        for page in range(1, 4):  # Scrape 10 pages
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            for product in soup.find_all('div', {'class': 'sg-col-inner'}):
                try:
                    title = product.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).text.strip()
                    price = product.find('span', {'class': 'a-price'}).find('span', {'class': 'a-offscreen'}).text.strip()
                    type_and_count = product.find('span', {'class': 'a-size-base a-color-base s-background-color-platinum a-padding-mini aok-nowrap aok-align-top aok-inline-block a-spacing-top-micro puis-medium-weight-text'}).text.strip()
                    date = datetime.now()  # Get the current date and time

                    # Insert or update product in database
                    c.execute("INSERT OR IGNORE INTO products (title, type_and_count) VALUES (?, ?)", (title, type_and_count))
                    c.execute("SELECT id FROM products WHERE title = ? AND type_and_count = ?", (title, type_and_count))
                    product_id = c.fetchone()[0]

                    # Insert price history
                    c.execute("INSERT INTO price_history (product_id, price, date) VALUES (?, ?, ?)", (product_id, price, str(date)))
                    conn.commit()

                    print(f'Title: {title}\nPrice: {price}\nType and Count: {type_and_count}\n--- \n{date}')
                except AttributeError:
                    continue

            # Slowly scroll to the bottom of the page
            slow_scroll_to_bottom(driver)

            # Wait for the "Next Page" button to become clickable
            next_page_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//a[@aria-label='Go to page {page + 1}']"))
            )
            next_page_button.click()
            time.sleep(2)  # Wait for the next page to load
    finally:
        # Close the connection
        conn.close()
        driver.quit()  # Close the WebDriver

search_term = input('Enter product to search for : \n')
scrape_amazon(search_term)