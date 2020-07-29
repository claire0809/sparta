print("hello, Sparta")
a = 3
print(a)
b = a
print(b)

a = a+1
print(a)
print(a)

print (a)

num1 = a * b
print(num1)

num2 = 99
print(num2)

name = "Harry"
print(name)

num = 12
print(num)

number_status = "true"
print(number_status)

number_stat = True
print(number_stat)

a_list = []
print(a_list)

a_list.append(1)
print(a_list)

a_list.append([2,3])
print(a_list)

a_list.append("me")
print(a_list)

print(a_list[0])
print(a_list[1])
print(a_list[1][0])

a_dict ={}
print(a_dict)

wizard = {"name" : "Harry Potter", "age" : 40}
print(wizard)

wizard["height"] = 173
print(wizard)

wizards = [{"name" : "HarryPotter", 'age' : 40},{'name' : 'Ron Weasley', 'age' : 40}]
print(wizards)

print(wizards[0]["name"])
print(wizards[1]['name'])

new_wizard = {'name' : 'Albus Potter', 'age' : 14}
wizards.append(new_wizard)
print(wizards)
print(wizards[2]["name"])

def sum_all(a,b,c):
    return a+b+c

print(sum_all(2,3,4))

def mul(a,b):
    return a*b
print(mul(2,3))

result = sum_all(2,3,4) + mul(10,10)
print(result)

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

num_twenty = is_even(20)
print(num_twenty)
is_even(27)

def is_adult(age):
    if age >= 20:
        print("성인입니다")
    else:
        print('미성년자입니다')

is_adult(10)
is_adult(45)

def check_generation(age):
    if(age >120):
        print("와 19세기에 태어나셨군요!")
    elif(age > 80):
        print("80세 이상! 인생은 여든부터!")
    else:
        print('젊으시군요! 장래희망이 뭔가요?')

my_age = 55
check_generation(my_age)

fruits = ['사과','배','감','귤']
for fruit in fruits:
    print(fruit)

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
count = 0
for apple in fruits:
    # print(apple)
    if apple == "사과":
        count += 1

print(count)

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
def count_fruit(name):
    count = 0
    for fruit in fruits:
        if fruit == name:
            count +=1
    return count

print(count_fruit("수박"))
gam_count = count_fruit("감")
print(gam_count)

wizards = [
    {'name': '해리', 'age': 40},
    {'name': '허마이오니', 'age': 40},
    {'name': '론', 'age': 41},
]

# print(wizards)

for wizard in wizards:
    print(wizard["name"], wizard["age"])


professor_wizards = [
    {'name': '덤블도어', 'age': 116},
    {'name': '맥고나걸', 'age': 85},
    {'name': '스네이프', 'age': 60},
]

# def get_age(name):
#     for professor_wizard in professor_wizards:
#         if professor_wizard["name"] == name:
#             return professor_wizard["age"]
#     return "해당하는 이름이 없습니다"
# print(get_age("맥고나걸"))

def get_age(name, wizards):
    # wizards! 윗 줄 함수 선언에서 사용한 변수죠? 함수 사용하는 쪽에서 쓰는 변수명 아닙니다!
    for wizard in wizards:
        if wizard['name'] == name:
            return wizard['age']
    return '해당하는 이름이 없습니다'


print(get_age("해리", wizards))
print(get_age('맥고나걸', professor_wizards))



