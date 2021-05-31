# Python script to automate signup for leftover vaccines in Region Midt

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
start_url = "https://www.auh.dk/om-auh/tilbud-om-covid-vaccination-ved-brug-af-restvacciner/"
driver.get(start_url)


name_field = '//*[@id="06ea46a4-9fe2-49c0-b3fa-9217ab3e3c0e"]'
dob_field = '//*[@id="56930c3b-65ef-4e63-bb15-27a36a4256b8"]'
email_field = '//*[@id="db67108b-6627-43d7-982e-2b11c6b5b26e"]'
phone_field = '//*[@id="41df7f89-d7b9-4203-b18a-8f4c86023f89"]'
location = '//*[@id="a268ffc4-333e-4813-ae3f-9d9f40c40200"]/fieldset/label[2]/input'
send = '//*[@id="58efbdd7-1555-4202-aec4-30c5745c4797"]'

driver.find_element_by_xpath(name_field).send_keys("NAME")
driver.find_element_by_xpath(dob_field).send_keys("DD/MM/YYYY")
driver.find_element_by_xpath(email_field).send_keys("EMAIL")
driver.find_element_by_xpath(phone_field).send_keys("PHONE NUMBER")
driver.find_element_by_xpath(location).click()
driver.find_element_by_xpath(send).click()
