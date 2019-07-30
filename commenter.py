import praw
import re
import os
import time
import random as rando
from common import clear
from praw.models import Message
from readinbox import readInbox

posts_replied_to = []
numbers = range(1,1000)
reddit=praw.Reddit('bot1')
def commenter():
    subreddit = reddit.subreddit('all')
    while True:
        for submission in subreddit.new(limit=2):
            if re.search("", submission.title, re.IGNORECASE):
                print(submission.title)
                upvote = input("Would you like to upvote this post?")
                decider = rando.choice(numbers)
                if decider > 500 and upvote == "y":
                    submission.upvote()
                    upvote = True
                print("Bot interacting with:", submission.title,"\n")
                print("Submission ID: ",submission.id,"\n")
                print("The author is:",submission.author,"\n")
                print("the post's score is:",submission.score,"\n")
                print("The decider is:",decider,"\n")
                if upvote == True:
                    print("I upvoted\n")
                author = str(submission.author)
                if reddit.redditor(author).has_verified_email == True and decider > 500 and upvote == True:
                    if submission.id not in posts_replied_to:
                        reddit.redditor(author).message("Hey", "I hope you have a great day")
                        posts_replied_to.append(submission.id)
                        print("I PM'd", submission.author)
                print("\n")
                time.sleep(2)
                clear()
                readInbox()
