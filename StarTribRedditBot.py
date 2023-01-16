import praw
import os

reddit = praw.Reddit(client_id=os.environ.get('BOT_CLIENT_ID'),
                     client_secret=os.environ.get('BOT_CLIENT_SECRET'),
                     user_agent='Star Tribune Paywall Bot v1.0 by u/MagicMikeyMike')

userComments = {}
user = reddit.redditor('The_Decoy')
url = 'https://www.reddit.com/r/CommunismMemes/comments/10d4l7f/all_i_know_is_you_guys_love_the_color_red/'

for link in user.comments.new(limit=None):
    userComments[link.link_permalink] = link.link_permalink
print("done loading")

if url in userComments.keys():
    print(userComments[url])


# subreddit = reddit.subreddit('Minneapolis')
#
# for post in subreddit.hot(limit=100):
#     hasComment = False
#     if hasattr(post, 'url_overridden_by_dest'):
#         if post.url_overridden_by_dest.lower().__contains__('startribune'):
#             print(post.url_overridden_by_dest)
#             break
