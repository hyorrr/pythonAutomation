from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

    # 비밀번호 저장/팝업 끄기
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    service = Service("/Users/songhyolim/PycharmProjects/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")

    return driver

def login():
    driver = get_driver()
    driver.find_element(By.ID, "CustomerEmail").send_keys("ssdu0114@naver.com")
    time.sleep(1)
    driver.find_element(By.ID, "CustomerPassword").send_keys("(I%5$8LA9")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="customer_login"]/button').click()
    return driver

def go_to_contact_us():
    driver = login()
    driver.find_element(By.XPATH, '//*[@id="shopify-section-footer"]/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
    time.sleep(1)


def main():
    time.sleep(1)
    go_to_contact_us()


if __name__ == '__main__':
    main()