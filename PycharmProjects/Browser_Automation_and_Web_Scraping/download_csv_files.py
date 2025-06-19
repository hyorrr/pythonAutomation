import requests

format_data = input("Enter the format annual or monthly: ")

url = f"https://datahub.io/core/global-temp/_r/-/data/{format_data}.csv"
# https://datahub.io/core/global-temp/_r/-/data/annual.csv
# https://datahub.io/core/global-temp/_r/-/data/monthly.csv

# 해당 URL에 HTTP GET 요청을 보냄. (즉, 그 주소에 접속해봐! 하는 거야)
# 응답 결과(=웹서버에서 받은 데이터)를 바이트(bytes) 형태로 가져옴.
content = requests.get(url).content
#print(content)

# 파일을 쓰기(write) 모드로 열되, '바이너리(binary)'로 열겠다는 뜻
with open('.venv/data.csv', 'wb') as file:
    file.write(content)

https://stooq.com/q/l/?s=ale&f=sd2t2ohlcv&h&e=csv