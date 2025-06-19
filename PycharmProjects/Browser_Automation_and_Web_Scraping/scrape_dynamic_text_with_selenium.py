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

def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    time.sleep(2) # 특정값을 받아오기위해 멈추기
    # How to deal with dynamic values -> hard coding 직접 XPATH 경로 찾아나서 or copy full XPATH
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
    # .text -> 웹 요소 객체 안(element 안) 에 있는 텍스트 추출
    return clean_text(element.text)

print(main())
# if __name__ == '__main__':
#     main()