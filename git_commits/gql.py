import requests
import json
import writedb 
from writedb import writedb

class Main:
  def git_activities():
    api_token = "xxxxxxxxxxxxxxxxxxxxxxxxx"

    url = 'https://api.github.com/graphql'

    json = { "query" : """{ 
    repository(owner:"bitcoin",name:"bitcoin"){
        nameWithOwner
      watchers{
          totalCount
          
        }


      forkCount
      stargazers{
        totalCount
      }
      
      object(expression:"master"){

      
        ... on Commit {
          history(first:10){
            
            totalCount
            edges{
              node{
                committedDate
                committer {
                  date
                  name

                }
                messageHeadline           
              }
            }
          }
        }
      }
    }  
    }


    """ }

    headers = {'Authorization': 'token %s' % api_token}
    r = requests.post(url=url, json=json, headers=headers)

    print(r.status_code)
    reply = r.json()


    return reply


    # ###    https://api.github.com/repos/bitcoin/bitcoin/contributors == 29 contributors given
