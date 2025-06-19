from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_curency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_curency}&amount=1'
    #print(url)

    # 웹페이지의 HTML 원본 소스 전체를 문자열로 보여줌
    content = requests.get(url).text
    #print(content)

    soup = BeautifulSoup(content, 'html.parser')
    #print(soup)

    # currency = soup.find("span", class_="ccOutputRslt")
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[0:-4])

    return rate

print(get_currency('INR', 'USD'))
print(get_currency('KRW', 'EUR'))