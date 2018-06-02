import pymysql
pymysql.install_as_MySQLdb()

import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","password","reddit" )


# prepare a cursor object using cursor() method
cursor = db.cursor()

class writedb:
    
  def write_commit(committer,date,message,repo):
    sql_commit ="INSERT INTO git_commit(commiter, date, message, repository) VALUES(%s, %s, %s, %s)"
    cursor.execute(sql_commit,(committer,date,message.encode('utf-8'),repo))
    try:
      db.commit()
    except:
      db.roolback()
      print("ERROR in writing comments")

  def write_repo(repository,forks,stars,watcher,commit_count):
    sql_repo ="INSERT INTO git_repo(repository, forks, stars, watcher, commit_count) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(sql_repo,(repository,forks,stars,watcher,commit_count))
    try:
      db.commit()
    except:
      db.roolback()
      print("ERROR in writing repo")


  def update_repo(repository,forks,stars,watcher,commit_count):
    cursor.execute ("""
      UPDATE git_repo
      SET repository=%s, forks=%s, stars=%s, watcher=%s, commit_count=%s
      WHERE repository=%s
    """, (repository, forks, stars, watcher, commit_count, repository))
    db.commit()

  def insert_new(commiter,date,message,repo):
    sql_check = "SELECT * FROM git_commit WHERE (commiter=(%s) AND date=(%s) AND message=(%s) AND repository=(%s) )"
    cursor.execute(sql_check,(commiter,date,message.encode('utf-8'),repo))
    entry = cursor.fetchone()

    if entry is None:
      sql_new = "INSERT INTO git_commit (commiter, date, message, repository) VALUES (%s, %s, %s, %s)"
      cursor.execute(sql_new,(commiter,date,message.encode('utf-8'),repo))
      db.commit()
    else:
      print('found')    

  # insert_new('commiter','date','message','repo')
  # update_repo('bitcoin/bitcoin',1,1,1,1)

