from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set options to make browsing easier
def get_driver():
    options = webdriver.ChromeOptions()
    # 현재 버전에서는 더 이상 지원되지 않음
    # options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    #options.add_argument("disable-dev-shm-usage")
    #options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    service = Service("/Users/songhyolim/PycharmProjects/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com")

    time.sleep(5)
    return driver

def main():
    driver = get_driver()
    #element = driver.find_element(by="Xpath", value="/html/body/div[1]/div/h1[1]")
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")

    return element.text

print(main())
# if __name__ == '__main__':
#     main()