from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),

                          options=options)

driver.get("https://sinov8.net")
driver.maximize_window()

links = driver.find_elements("xpath", "//a[@href]")
for link in links:
    print(link.get_attribute("innerHTML"))
    if "Software Solutions" in link.get_attribute("innerHTML"):
        link.click()
        break

    
                                                    