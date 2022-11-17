from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import bs4
from datetime import datetime

options = Options()
options.headless = True
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
driver.maximize_window()
driver.get("https://forces.ca/en/careers")

# Clicky
dropdown = '//*[@id="btn-filter-menu"]'
indemand = '//*[@id="filter-menu-dropdown"]/div[1]/div[5]/div/button'
label = '//*[@id="filter-menu-inDemand"]/div/ul/li[1]/label'
closer = '//*[@id="filter-modal"]/div/div/div[1]/button'

driver.implicitly_wait(30)

driver.find_element(By.XPATH, dropdown).click()

driver.find_element(By.XPATH, indemand).click()

driver.find_element(By.XPATH, label).click()

driver.find_element(By.XPATH, closer).click()

file = driver.page_source

driver.quit()


soup = bs4.BeautifulSoup(file, "html.parser")

job_titles = soup.find_all("h2", {"class": "job-card-title"})
formated_job_titles = [job.text for job in job_titles]

MAX_LEN = len(sorted(formated_job_titles, key=len)[-1])

print(f"There are currently \
{len(formated_job_titles)} in-demand job postings on the CAF website.\n")

print("They are:")
for c,v in enumerate(formated_job_titles):
    print(f"{c+1}. {v.ljust(MAX_LEN)}")

with open(f"{datetime.today().strftime('%Y-%m-%d')}outputs.txt", "w", encoding="utf-8") as f:
    for c,v in enumerate(formated_job_titles):
        f.write(f"{c+1} {v}{' ' * MAX_LEN}\n")
