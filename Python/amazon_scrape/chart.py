import sqlite3
import re
import matplotlib.pyplot as plt

def on_click(event, titles, price_history):
    if event.inaxes == ax:
        index = int(event.xdata)
        title = titles[index]
        pid = ''  # Set an empty string for product ID since it's not available
        history = price_history[index]
        prices = [float(re.sub(r'[^\d.]', '', price)) for price in history.split(' | ')]
        plt.figure(figsize=(8, 6))
        plt.plot(prices, marker='o', color='b')
        plt.xlabel('Price Update Index')
        plt.ylabel('Price')
        plt.title(f'Price History for {title}')
        plt.grid(True)
        plt.show()

# Connect to the SQLite database
conn = sqlite3.connect('amazon_data.db')
cursor = conn.cursor()

# Fetch data of product title, total price changes, product ID, and price history from the price_history table
cursor.execute("""
    SELECT p.id, p.title, SUM(CAST(REPLACE(ph.price, '$', '') AS REAL)) AS total_price_change, GROUP_CONCAT(ph.price, ' | ') AS price_history
    FROM price_history AS ph
    INNER JOIN products AS p ON ph.product_id = p.id
    GROUP BY p.id, p.title
    ORDER BY total_price_change DESC
    LIMIT 10  -- Adjust the limit as per your requirement
""")

# Fetch all the rows
rows = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()

# Extract product IDs, titles, total price changes, and price history from the fetched rows
product_ids, titles, total_price_changes, price_history = zip(*rows)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Subplot for total price changes
ax.bar(range(len(titles)), total_price_changes, color='skyblue')
ax.set_ylabel('Total Price Changes')
ax.set_title('Products with the Largest Total Price Changes')
ax.set_xticks(range(len(titles)))
ax.set_xticklabels(titles, rotation=45, ha='right')

# Connect the on_click function to the figure
fig.canvas.mpl_connect('button_press_event', lambda event: on_click(event, titles, price_history))

# Show the plot
plt.show()