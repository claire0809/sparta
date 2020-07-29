from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

# (2) 월-e의 평점과 같은 평점으 영화 제목들을 가져오기
# movies: 몽고d 컬렉션 이름.
movie = db.movies.find_one({"title" : "월-E"})
print(movie)
print(movie["star"])
target_star = movie['star']

target_movies = list(db.movies.find({'star': target_star}))



    # movie_stars = list(db.movies.find())
    # print(movie_star["star"])
    #
    # for movie_star in movie_stars:
    #
    # # if (movie_star) == movie["star"]:




# (3) 월-e의 평점과 같은 평점의 영화 제목을 0으로 만들기.  >>>update 해주면 됨
# 선생님 방법.
for target_movie in target_movies:
    print(movie['title'])
    db.movies.update_one(target_movie, {"$set": {"star": 0}})

# 교재 방법: update_many 를 쓴 것도 확인. (통신이 적기 때문에 더 빠를 것.)
for target_movie in target_movies:
    print(movie['title'])

db.movies.update_many({"star": target_star}, {"$set": {"star" : "1"}})