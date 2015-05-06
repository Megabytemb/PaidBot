import praw
import argparse
import time
import re
import logging

parser = argparse.ArgumentParser()

parser.add_argument('-u', action='store', dest='username',
                    help='Reddit Bot Username')
parser.add_argument('-p', action='store', dest='password',
                    help='Reddit Bot Password')

results =  parser.parse_args()

checked = set()

error = re.compile(r'\bpayed\b', re.IGNORECASE)

correction = "~~payed~~ paid"

def Loop(reddit):
    try:
        count = 0
        #subreddit = reddit.get_subreddit('test')
        #all_comments = subreddit.get_comments(limit=1000)
        all_comments = reddit.get_comments('all', limit=None)
        for comment in all_comments:
            count +=1
            comment_id = comment.link_id[3:]
            if error.search(comment.body) is not None and comment_id not in checked:
                checked.add(comment_id)
                comment.reply(correction)
                
                print "Found Something"
                print comment.permalink
            else:
                pass
        timeset = time.strftime("%m-%d %H:%M:%S") # current date and time
        print timeset
        print "Just scanned " + str(count) + " comments.\n"
    except Exception as e:
        print str(e)

def main():
    reddit = praw.Reddit(user_agent="Python:PaidB0t:1.0 (by /u/megabytemb)", cache_timeout=0, api_request_delay=1.0)
    reddit.login(username=results.username, password=results.password)
    
    while True:
        Loop(reddit)
        
if __name__ == "__main__":
    main()
