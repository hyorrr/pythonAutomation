from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Service 객체 생성 (여기서 str → Service로 감싸줘야 함!)
service = Service("/Users/songhyolim/PycharmProjects/chromedriver")

# WebDriver 실행
driver = webdriver.Chrome(service=service)


# 웹사이트 열기
driver.get("https://www.google.com")

# 구글 검색창에 텍스트 입력
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Hello Selenium!")
search_box.submit()

time.sleep(3)

# 종료
driver.quit()
