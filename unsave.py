import praw
import pdb
import re
import os
import time
import random as rando



reddit = praw.Reddit('bot1')
def unsave():
    saved = reddit.user.me().saved(limit=1000)
    for s in saved:
      try:
        s.unsave()
        print("Unsaved post")
      except AttributeError as err:
        print(err)
    print("Unsaved all posts")
unsave()
