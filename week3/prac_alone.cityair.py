# import requests
#
# response_data = requests.get("http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99")
#
# city_air = response_data.json()
#
# # print(city_air["RealtimeCityAir"]["row"][0]['NO2'])
# print(city_air["RealtimeCityAir"]["row"])


import requests
response_data = requests.get("http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99")
cityAir = response_data.json()
print(cityAir)
for key in cityAir.keys():
    cityAir[key]
# for city in cityAir:
    # print(city[])
# ** 질문왜 RESULT 하고 row 하고 나오지 않지? 왜 RealtimeCityAir만 나오는지? 리스트가 아니라, 딕셔너리라서 FOR문 안되나?

gu_infos = cityAir["RealtimeCityAir"]["row"]

for gu_info in gu_infos:
    print(gu_info["MSRSTE_NM"], gu_info["PM10"])


# import requests
# response_data = requests.get("http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99")
# cityair = response_data.json()
# gu_infos = cityair["RealtimeCityAir"]["row"]
#
# for gu_info in gu_infos:
#     if gu_info["PM10"] < 20:
#         print(gu_info["MSRSTE_NM"], gu_info["PM10"])







