import csv
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
from selenium.common.exceptions import NoSuchElementException

browser_driver = Service(r'C:\Users\shiro\AppData\Local\Programs\Python\Python310\geckodriver.exe')
page_to_scrape = webdriver.Firefox(service=browser_driver)
page_to_scrape.get("http://quotes.toscrape.com")

page_to_scrape.find_element(By.LINK_TEXT, "Login").click()

time.sleep(3)
username = page_to_scrape.find_element(By.ID, "username")
password = page_to_scrape.find_element(By.ID, "password")
username.send_keys("admin")
my_pass = getpass.getpass()
password.send_keys(my_pass)
page_to_scrape.find_element(By.CSS_SELECTOR, "input.btn-primary").click()

file = open("scraped_quotes.csv", "w", encoding= "utf-16")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

while True:
    quotes = page_to_scrape.find_elements(By.CLASS_NAME, "text")
    authors = page_to_scrape.find_elements(By.CLASS_NAME, "author")
    for (quote, author) in zip(quotes, authors):
        print(quote.text, "-" + author.text)
        writer.writerow([quote.text, author.text])
    try:
        page_to_scrape.find_element(By.PARTIAL_LINK_TEXT, "Next").click()
    except NoSuchElementException:
        break
        
file.close()