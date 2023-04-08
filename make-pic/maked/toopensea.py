from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
options = Options()
driver = Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.get(
    "https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn")
time.sleep(1)
element = driver.find_element(
    By.CLASS_NAME, "g-c-R")
element.click()


driver.get("https://opensea.io/login?referrer=%\\2Faccount")
time.sleep(1)
element = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/main/div/div/div/div[2]/ul/li[1]")
element.click()
pass
