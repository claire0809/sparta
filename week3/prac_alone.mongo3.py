from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

# worry = db.movies.find_one({'title' : '월-E'}, {'_id' : False})
# print(worry)

movies = list(db.movies.find({}))
print(movies)

wal_e = db.movies.find_one({'title' : '월-E'})
print(wal_e)
print(wal_e['star'])


# 월-E의 평점과 같은 평점의 영화 제목들을 가져오기
# for wal_e in movies:
#     print(wal_e)
# !주의! for문 쓸 때 콜론 빼먹지 말기!!!

# # same_star = db.movies.find
# if 점수 == (wal_e['star'])
#     print(타이틀... )

# title = movies[1]["title"]
# print(title)

print( list(db.movies.find({"star" : wal_e['star']})) )

same_stars = list(db.movies.find({"star" : wal_e['star']}))
print(same_stars)
for same_star in same_stars:
    print(same_star['title'])



#**질문: if문을 사용해서 월-E의 평점과 같은 평점의 영화 제목을 가져올 수는 없는지??
# for wal_e in movies:
#     print(wal_e)
    # if {'star': 9.35} :
    #     print(db.movies.find_one({'star'}))


# 월-E의 평점과 같은 평점의 영화 제목들의 평점을 0으로 만들기
zero_star = db.movies.update_many({'star' : wal_e['star']}, {'$set': {'star' : 0}})
print(zero_star)