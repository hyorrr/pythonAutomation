from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import os

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

def update_temperature_and_save_to_file(driver):
    while True:
        current_temperature = driver.find_element(By.ID, "displaytimer")
        current_temperature_text = current_temperature.text
        output = float(current_temperature_text.split(": ")[1])

        now = datetime.now()  # 예: 2025-06-11 02:35:44
        file_name = now.strftime("%Y%m%d_%H%M%S") + ".txt"  # 파일명을 문자열로 변환

        with open(file_name, "w") as f:
            # open: 파일을 여는 함수 (파일 객체를 반환함)
            # with: 파일 열고 나면 자동으로 닫아주는 안전한 문법
            # as f: open()으로 얻은 파일 객체에 f라는 이름을 붙임
            f.write(f"Current Temperature is: {output}")  # 그 별명(f)을 이용해 파일에 글을 씀
            f.flush()  # 💡 버퍼를 강제로 비워서 디스크에 바로 기록, (물리 디스크까지는 아직)
            os.fsync(f.fileno())  # 💾 진짜 물리 디스크에 바로 씀

        time.sleep(2)

# def clean_text(text):
#     output = float(text.split(": ")[1])
#     return output

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

    return update_temperature_and_save_to_file(driver)

    # current_temperature = driver.find_element(By.ID, "displaytimer")
    # return save_to_file(current_temperature.text)

print(main())
# if __name__ == '__main__':
#     main()