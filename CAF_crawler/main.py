from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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

CLASS_NAME = "class name"
# Get the job titles

job_titles = driver.find_elements(By.CLASS_NAME, "job-card-title")
print([job.text for job in job_titles])
driver.quit()
