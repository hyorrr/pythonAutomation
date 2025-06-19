from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime as dt

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
    temperature = float(text.split(": ")[1])
    return temperature

def write_file(current_temperature):
    """Write current_temperature into a text file"""
    filename = f"{dt.now().strftime("%Y-%m-%d.%H-%M-%S")}.txt"
    with open(filename, "w") as file:
        file.write(current_temperature)

def main():
    driver = get_driver()
    while True:
        time.sleep(2) # 특정값을 받아오기위해 멈추기
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
        current_temperature = str(clean_text(element.text))
        write_file(current_temperature)

print(main())
# if __name__ == '__main__':
#     main()