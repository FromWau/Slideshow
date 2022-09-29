import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

URLS = ['https://www.144.at/webansicht/dienststelle-2000357570_1.html','http://10.0.0.4:8080/CheckedVehicles/Traismauer']
refreshrate = 5
gecko_path='/usr/bin/geckodriver'


firefox = Service(gecko_path)
options = webdriver.FirefoxOptions()
options.set_preference("security.fileuri.strict_origin_policy", False)
driver = webdriver.Firefox(service=firefox, options=options)
driver.fullscreen_window() 

while True:
    for url in URLS:
        driver.get(url)
        time.sleep(refreshrate)
