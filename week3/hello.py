print("hello python")
a = 1
hello = 2
print(hello)
bye = True
a_list = []
a_list.append(1)
print(a_list)

fruits = ['사과', '배', '감', '귤']

for fruit in fruits:  # fruit 은 우리가 임의로 지어준 이름입니다. 변수임. 이름 바꿔도 됨.
    print(fruit)  # 사과, 배, 감, 귤 하나씩 꺼내어 출력합니다.

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

# count = 0
# for fruit in fruits:
#     if fruit == '사과':
#         count += 1
#
# # 사과의 갯수를 출력합니다.
# print(count)
#
# counts = 0
# for fruit in fruits:
#     if fruit == "사과" :
#         count+=1
#
# print(count)
# print(count)

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

#  왜 배가 안세질까... 배 다시 세보기. 3이 나와야 하는데, 0이 나옴.
def count_fruits(name):
    count =0
    for fruit in fruits:
        if fruit is name:
            count += 1
        return count

print(count_fruits("배"))


wizards = [
{'name': '해리', 'age': 40},
{'name': '허마이오니', 'age': 40},
{'name': '론', 'age': 41},
]

for wizard in wizards:
    print(wizard["name"])
    print(wizard["age"])

