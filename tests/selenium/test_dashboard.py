from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://localhost:5601")
assert "Wazuh" in driver.title
driver.quit()
