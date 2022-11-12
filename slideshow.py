import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException, InvalidSessionIdException


URLS = [
    'https://www.144.at/webansicht/dienststelle-2000357570_1.html',
    'http://10.0.0.4:8080/CheckedVehicles/Traismauer'
]
refreshrate = 5
gecko_path='/usr/bin/geckodriver'


firefox = Service(gecko_path)
options = webdriver.FirefoxOptions()
options.set_preference("security.fileuri.strict_origin_policy", False)
driver = webdriver.Firefox(service=firefox, options=options)


while True:

    for url in URLS:
        try:
            driver.fullscreen_window() 
            driver.get(url)

        except InvalidSessionIdException as e:
            print("Error -- window got propably killed")
            print("Traceback:")
            print(e)
            exit(1)

        except WebDriverException: 
            print("Skipping -- Unable to reach: " + url)       
            time.sleep(1)
            break

        except Exception as e:
            print("Traceback:")
            print(e)
            time.sleep(1)
            break

        time.sleep(refreshrate)
