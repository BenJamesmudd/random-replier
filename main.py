import praw
import re
import os
import time
import random as rando
from commenter import commenter
from common import clear
from readinbox import readInbox

reddit=praw.Reddit('bot1')

commenter()
