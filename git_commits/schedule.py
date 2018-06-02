import schedule
import time
from gql import Main
import configparser
import json
from jsondiff import diff
from writedb import writedb
import pandas as pd
from pandas import DataFrame


config = configparser.RawConfigParser()
config.read('refresh_time.cfg')
interval = config.getint('Main','time')
t = int(interval)

response = Main.git_activities()


new = response['data']['repository']
namewithowner = new['nameWithOwner']
watchers = new['watchers']['totalCount']
fork = new['forkCount']
stars = new['stargazers']['totalCount']
commit_count = new['object']['history']['totalCount']
commit = new['object']['history']['edges']
writedb.write_repo(namewithowner,fork,stars,watchers,commit_count)


for each in commit:
  date = each['node']['committedDate']
  committer = each['node']['committer']['name']
  message = each['node']['messageHeadline']
  writedb.write_commit(committer,date,message,namewithowner)


def job():
  
  response1 = Main.git_activities()
  time.sleep(300)
  response2 =Main.git_activities()
  r = diff(response1,response2)
  df = DataFrame(response1)
  df2 = DataFrame(response2)
  ne = (df != df2).any(1)
  print(ne)
  if r=={}:
    print('no difference in git activites from last response')
  else:
    print('difference')
    new = response2['data']['repository']
    namewithowner = new['nameWithOwner']
    watchers = new['watchers']['totalCount']
    fork = new['forkCount']
    stars = new['stargazers']['totalCount']
    commit_count = new['object']['history']['totalCount']
    commit = new['object']['history']['edges']
    writedb.update_repo(namewithowner,fork,stars,watchers,commit_count)

    for each in commit:
      date = each['node']['committedDate']
      committer = each['node']['committer']['name']
      message = each['node']['messageHeadline']
      writedb.insert_new(committer,date,message,namewithowner)
  

while True:
  job()

