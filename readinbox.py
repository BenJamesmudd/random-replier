import praw
import pdb
import re
import os
import time
import random as rando
from common import clear
from praw.models import Message
from praw.models import Inbox


def readInbox():
    reddit=praw.Reddit('bot1')

    for x in range(1):
        for message in reddit.inbox.unread(limit=10):
            print(message.body , "\n")
            author = str(message.author)
            subject_of_msg = input("What would you like the subject of the reply to be?\n")
            body_of_msg = input("What would you like the body of the reply to be?\n")
            reddit.redditor(author).message(subject_of_msg , body_of_msg)
            print("Message Sent To:",author)
            message.mark_read()
            clear()
