import redis
import datetime
import sys

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432

def article_vote(redis, user, article):
    cutoff = datetime.datetime.now() - datetime.timedelta(seconds=ONE_WEEK_IN_SECONDS)

    if not datetime.datetime.fromtimestamp(redis.zscore('time:', article)) < cutoff:
        article_id = article.split(':')[-1]
        if redis.sadd('voted:' + artical_id, user):
            #redis.zincrby('score:', VOTE_SCORE, article)
            redis.zincrby('score:', article, VOTE_SCORE)
            redis.hincrby(article, 'votes', 1)

def article_switch_vote(redis, user, from_article, to_article):
    #cutoff = datetime.datetime.now() - datetime.timedelta(seconds=ONE_WEEK_IN_SECONDS)
    #if not datetime.datetime.fromtimestamp(redis.zscore('time:',to_article)) < cutoff:
    	from_article_id = from_article.split(':')[-1]
	to_article_id = to_article.split(':')[-1]
	if redis.sadd('voted:' + to_article_id, user) and redis.srem('voted:' + from_article_id, user): 
	    redis.zincrby('score:', to_article, VOTE_SCORE)
            redis.hincrby(to_article, 'votes', 1)
	    redis.zincrby('score:',from_article,(-1*VOTE_SCORE))
            redis.hincrby(from_article, 'votes',-1)
    # HOMEWORK 2 Part I
    # pass
redis = redis.StrictRedis(host='localhost', port=6379, db=0)
# user:3 up votes article:1
article_vote(redis, "user:3", "article:1")
# user:3 up votes article:3
article_vote(redis, "user:3", "article:3")
# user:5 switches their vote from article:1 to article:0
article_switch_vote(redis, "user:2", "article:8", "article:1")

# Which article's score is between 10 and 20?
# PRINT THE ARTICLE'S LINK TO STDOUT:
# HOMEWORK 2 Part II
#article = redis.?
article = redis.zrangebyscore("score:", 10, 20)
print redis.hget(article[0], 'link')
