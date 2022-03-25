import praw
from datetime import datetime
import pandas as pd
import matplotlib
import pandas


reddit = praw.Reddit(
    username='',
    password='',
    client_id='',
    client_secret='',
    user_agent=''
)
subreddit = reddit.subreddit('soccer') 
list_link = []
submission_title = []
list_else = []

for submission in subreddit.stream.submissions():
    flair = submission.link_flair_text
    url = submission.url
    title = submission.title
    if flair == 'Media':
        list_link.append(url)
        submission_title.append(title)
        print(title)
        print(url)
        df = pd.DataFrame(list(zip(submission_title, list_link)), columns=['Title', 'Link'])
        df.to_csv('soccer_weekend_links.csv')
    else:
        list_else.append('No link')
