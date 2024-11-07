from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-certificate-errors')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

driver = webdriver.Chrome(options=options)

def scrape_profile(username):
    url = f"https://www.linkedin.com/in/{username}"
    driver.get(url)
    
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".pv-top-card__contact-info")))
        name = driver.find_element(By.CSS_SELECTOR, ".pv-top-card__name").text
        headline = driver.find_element(By.CSS_SELECTOR, ".pv-top-card__headline").text
        location = driver.find_element(By.CSS_SELECTOR, ".pv-top-card__location").text
        industry = driver.find_element(By.CSS_SELECTOR, ".pv-top-card__industry").text
        print(f"\nProfile Data for {name}:")
        
    except Exception as e:
        print(f"An error occurred while scraping profile data: {str(e)}")

scrape_profile("dhanarooban-life-journey")
driver.quit()