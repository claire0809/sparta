from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다. dbsparta 이름 바꿔도 o.k.

# # MongoDB에 insert 하기(create)
#
# # 'users'라는 collection에 데이터를 생성합니다.
# db.users.insert_one({'name': '덤블도어', 'age': 116})
# db.users.insert_one({'name': '맥고나걸', 'age': 795})
# db.users.insert_one({'name': '스네이프', 'age': 60})
# db.users.insert_one({'name': '해리', 'age': 40})
# db.users.insert_one({'name': '허마이오니', 'age': 40})
# db.users.insert_one({'name': '론', 'age': 40})

# doc = {'name': '론', 'age': 40}
# db.users.insert_one(doc) 해도 db.users.insert_one({'name': '론', 'age': 40})와 결과는 똑같음.

#collections이름 user에서 mongos로 바꿔보기.
# db.mongos.insert_one({"name" : "론", "age" : 80})



# MongoDB에서 데이터 모두 보기(read)
all_users = list(db.users.find({}))
# ** 질문(27,28라인): find({}) method 사용할 때 list 꼭 필요한지?. 리스트 없이 print(db.users.find({})) 하면 출력 안됨. & find_one에서 list는 필요 없는지?
print(all_users)
print(db.users.find({}))


# print(all_users[2])  # 2번째 결과값을 보기
# print(all_users[0]['name'])  # 0번째 결과값의 'name'을 보기

# for user in all_users:  # 반복문을 돌며 모든 결과값을 보기
    # print(user)

# user = db.users.find_one({'name': '맥고나걸'})
# print(user)

same_ages = list(db.users.find({"age" : 40}))
# print(same_ages)

# for same_age in same_ages:
#     print(same_age)

# professor = db.users.find_one({"name" : "덤블도어"}, {"_id" : 0})
# print(professor)
#
db.users.update_one({"name" : "맥고나걸"}, {"$set" : {"age" : 25}})
mag=db.users.find_one({"name" : "맥고나걸"})
print(mag)


db.users.delete_one({"name" : "해리"})
user = db.users.find_one({"name" : "해리"})
print(user)




