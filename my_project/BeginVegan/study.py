a = "javascript:FDP001M01.fn_dpViewHisBack('028128');"

number = a.split("'")[1]
print(number)

b = "javascript:FDP001M01.fn_dpViewHisBack('"
c = "');"


full_address = b + number + c
print(full_address)



# https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=028128&gubunFlag=M&ctgrCd=2020050005


# onclick="javascript:FDP001M01.fn_dpViewHisBack('028128');"

# https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=028128&gubunFlag=M&ctgrCd=2020050005&stamp=XLeCI
# https://www.hellonature.co.kr/fdp002.do?goTo=moduleToDpList&pageSize=10&nextSize=10&filterYn=N&gubunFlag=M&ctgrCd=2020050005&evCd=&dpItemListCntYn=Y&scrollTop=200&dpCnt=0&page=2&dataFlag=108&dataCd=2020050005&grpCd=ALL&mainGrpCd=ALL&stamp=XLeC