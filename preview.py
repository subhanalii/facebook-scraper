# preview.py

print("\n📌 Facebook Group Email Comment Scanner - Preview")
print("✅ This demo tool scans Facebook groups you're a member of, expands visible comments, and extracts emails for lead generation.")
print("\n🔧 Features:")
print("- Uses undetected_chromedriver and Selenium")
print("- Scrolls posts and opens comment threads")
print("- Extracts visible emails and saves to CSV/Excel")
print("- Skips duplicates and filters old posts (older than 12 months)")
print("- Designed for public group automation only")

print("\n📼 YouTube Demo: https://youtu.be/0hhBhh0npHM")
print("📧 Gmail: isubhanali3@gmail.com")
print("💼 Upwork: https://www.upwork.com/freelancers/~01b6c1b6819be875f2?mp_source=share")
print("💬 Discord: s.a3")

print("\n🧪 Sample Code Snippet:\n")

print('''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
time.sleep(10)

posts = driver.find_elements(By.CSS_SELECTOR, 'div.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z')
for post in posts:
    print(post.text[:100], '...')
''')
