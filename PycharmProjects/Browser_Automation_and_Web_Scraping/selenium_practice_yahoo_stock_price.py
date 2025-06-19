import requests
from bs4 import BeautifulSoup
import re
import time

#사람이 실제로 야후 사이트에 접속해서 종목 들어가고 → 버튼 누르면
#브라우저가 내부적으로 쿠키, 헤더, crumb(야후가 요구하는 일종의 보안 토큰)을 자동으로 같이 보냄
#근데 requests.get() 같은 순수 Python 코드에서는 그게 없음 → "unauthorized"
#[정석 방법] crumb + 쿠키 자동 추출해서 요청 보내기
#야후가 사용하는 보안 구조를 흉내 내는 방식
#crumb는 CSRF 방지용 토큰 같은 거

def get_crumb_and_cookie(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}/history"
    session = requests.Session()
    response = session.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    # crumb 찾기 (스크립트 내부에서 추출)
    for script in soup.find_all("script"):
        if "CrumbStore" in script.text:
            crumb = re.search(r'"CrumbStore":\{"crumb":"(.*?)"\}', script.text).group(1)
            return crumb, session.cookies.get_dict()

        return None, None

def download_yahoo_csv(symbol, start_epoch, end_epoch):
    crumb, cookies = get_crumb_and_cookie(symbol)
    if not crumb:
        print("crumb 추출 실패")
        return

    url = f"https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={start_epoch}&period2={end_epoch}&interval=1d&events=history&crumb={crumb}"
    print("요청 URL: ", url)

    response = requests.get(url, cookies=cookies)

    if response.status_code == 200:
        with open(f"{symbol}.csv", "wb") as f:
            f.write(response.content)
        print(f"save {symbol}.csv successfully!")
    else:
        print("failed download:", response.status_code)

symbol = "AAPL"
start_epoch = int(time.mktime(time.strptime("2021-01-01", "%Y-%m-%d")))
end_epoch = int(time.mktime(time.strptime("2021-12-31", "%Y-%m-%d")))

download_yahoo_csv(symbol, start_epoch, end_epoch)
