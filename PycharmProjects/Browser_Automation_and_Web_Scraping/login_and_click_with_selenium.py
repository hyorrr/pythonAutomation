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
    driver.get("http://automated.pythonanywhere.com/login/")

    return driver

def clean_text(text):
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    # send_keys method: keyboard input
    driver.find_element(By.ID, "id_username").send_keys("automated")
    time.sleep(1)
    # after input press the ENTER key
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    time.sleep(3)
    print(driver.current_url) # after login url was changed
    current_temperature = driver.find_element(By.ID, "displaytimer")
    #print(current_temperature.text)
    return clean_text(current_temperature.text)

print(main())
# if __name__ == '__main__':
#     main()