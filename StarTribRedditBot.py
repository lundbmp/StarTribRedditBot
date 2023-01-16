import praw
import os

reddit = praw.Reddit(client_id=os.environ.get('BOT_CLIENT_ID'),
                     client_secret=os.environ.get('BOT_CLIENT_SECRET'),
                     user_agent='Star Tribune Paywall Bot v1.0 by u/MagicMikeyMike')

subreddit = reddit.subreddit('Minneapolis')

for post in subreddit.hot(limit=100):
    hasComment = False
    if hasattr(post, 'url_overridden_by_dest'):
        if post.url_overridden_by_dest.lower().__contains__('startribune'):
            print(post.url_overridden_by_dest)
            break

