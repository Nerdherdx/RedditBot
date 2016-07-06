import praw

r = praw.Reddit(user_agent='RedditAI')
submission = r.get_subreddit('pcgaming').get_hot(limit=5)
print([str(x) for x in submission])

