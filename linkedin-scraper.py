from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3787393812&distance=25&geoId=101165590&keywords=intern&origin=JOB_COLLECTION_PAGE_KEYWORD_HISTORY&refresh=true&start=25")

job_listings = driver.find_elements(By.XPATH, '//*[@id="main-content"]/section[2]/ul/li')

with open('job_llistings.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Job Title', 'Address', 'Job Link'])

    for listing in job_listings:
        job_title_element = listing.find_element(By.CLASS_NAME, "sr-only")
        job_title = job_title_element.text
        print("Job Title:", job_title)
        address_element = listing.find_element(By.CLASS_NAME, "base-search-card__metadata")
        address = address_element.text

        print("Address:", address)
        link_element = listing.find_element(By.CLASS_NAME, "base-card__full-link")
        job_link = link_element.get_attribute('href')

        print("Job Link:", job_link)
        print("-" * 50)
        csv_writer.writerow([job_title, address, job_link])

driver.quit()