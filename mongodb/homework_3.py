#!/usr/bin/env python

import pymongo
import pprint
import json
from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017')
db = client.test

#Part A
db.movies.update_many(
	{"genres":{"$in":["Comedy"]},"rated":"NOT RATED"},
	{"$set":{"rated":"Pending rating"}}
)
#The following lines were used to test that the database update was a success
#test_of_update=db.movies.aggregate([
#        { "$unwind": "$genres"},
#        { "$match" :{"rated":"Pending rating","genres":"Comedy"}},
#        { "$group" :{"_id": {"genre":"$genres","rated":"$rated"},"count": {"$sum":1}}}
#])
#print(list(test_of_update))

#Part B
result=db.movies.insert_one(
	{"title": "Thor: Ragnarok",
	 "year": 2017,
	 "countries":["USA"],
	 "genres":["Action", "Adventure", "Comedy"],
	 "directors":["Taika Waititi"],
	 "imdb":{
		"id": 3501632,


		"rating":7.92,
		"votes":299213
	 }
	}
)

#Part C
comedy_count=db.movies.aggregate([
	{ "$unwind": "$genres"},
	{ "$match" :{"genres":"Comedy"}},
	{ "$group" :{"_id": "$genres","count": {"$sum":1}}}
])
print(list(comedy_count))

#Part D
rating_country=db.movies.aggregate([
	{ "$unwind": "$countries"},
        { "$match" :{"rated":"Pending rating","countries":"USA"}},
        { "$group" :{"_id":{"country":"$countries","rated":"$rated"},"count": {"$sum":1}}}
])
print(list(rating_country))

#Part E
p_1992={"Year": "1992",
       "President": "Bill Clinton",
       "Party":"Democrat"}
vp_1992={"Year": "1992",
        "Vice-President": "Al Gore",
        "Party":"Democrat"}
p_2000={"Year": "2000",
       "President": "George Bush",
       "Party": "Republican"}
vp_2000={"Year": "2000",
       "Vice-President": "Dick Cheney",
       "Party": "Republican"}
p_2008={"Year": "2008",
       "President": "Barack Obama",
       "Party":"Democrat"}
vp_2008={"Year": "2008",
       "Vice-President": "Joe Biden",
       "Party":"Democrat"}
p_2016={"Year":"2016",
        "President":"Donald Trump",
	"Party": "Republican"}
vp_2016={"Year":"2016",
        "Vice-President":"Mike Pence",
        "Party":"Republican"}
db.theprez.insert_one(p_1992)
db.theprez.insert_one(p_2000)
db.theprez.insert_one(p_2008)
db.theprez.insert_one(p_2016)
db.thevprez.insert_one(vp_1992)
db.thevprez.insert_one(vp_2000)
db.thevprez.insert_one(vp_2008)
db.thevprez.insert_one(vp_2016)
test1=db.theprez.aggregate([
	{"$lookup":
	{ "from": "thevprez",
	  "localField":"Year",
	  "foreignField":"Year",
	  "as":"Two Most Powerful People in World:"
	}
	}
])
test2=db.thevprez.aggregate([
        {"$lookup":
        { "from": "theprez",
          "localField":"Party",
          "foreignField":"Party",
          "as":"Most Recent Presidents of his Party:"
        }
        }
])
print(list(test1))
print(list(test2))
