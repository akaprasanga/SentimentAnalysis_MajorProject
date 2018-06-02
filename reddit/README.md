# reddit_scrape


This script uses Python Reddit API Wrapper(PRAW). So installation of praw in your virtual environment is recommended.

TO INSTALL PRAW:

In terminal : pip3 install praw

TO USE THE reddit.py SCRIPT

In terminal : python3 -r name_of_subreddit	OR
In terminal : python3 -u url_of_subreddit

#Create DATABASE name 'reddit'

Tables:'submission','comments'

Columns of Submission:id(varchar),title(textutf8),author(varchar),karma(varchar),ups(varchar),downs(varchar),score(varchar)

Columns of comments:id(varchar),parent_id(varchar),text(text-utf8),submission_id(varchar)
