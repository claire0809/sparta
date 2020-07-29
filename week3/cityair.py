import requests  # requests 라이브러리 설치 필요(python requests 사용법 구글링)

# # requests 를 사용해 요청(Request)하기. 자바스크립트보다 파이썬의 requests를 이용해 get 을 하는 것이 간편.
# response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
#
# # 응답(response) 데이터인 json을 쉽게 접근할 수 있게 만들어 city_air 에 담고
# (자바스크립트랑 비교하자면, .json() 같은 구조는 자바스크립트에는 없음.
# json 자체가 JavaScript object notation 이기 때문에 자바스크립트에서는 파일 불러올 때 별도의 .json()이 필요 없지만...
# 파이썬에서는 json을 읽을 수 없기 때문에 파이썬이 읽을 수 있는 구조로 바꿔주는 과정
# city_air = response_data.json()
#
# # 값을 출력
# print(city_air['RealtimeCityAir']['row'][0]['NO2'])

import requests

response_data = requests.get("http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99")
city_air = response_data.json()

gu_infos = city_air["RealtimeCityAir"]["row"]
for gu_info in gu_infos:
    print(gu_info["MSRSTE_NM"], gu_info["PM10"])

