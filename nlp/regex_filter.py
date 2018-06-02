import re
import time

# create a empty temporary file
temp = open("temp.txt",'a').close()
final = open("final.txt",'a').close()

fname = 'labeledTweetData.csv'
with open(fname) as f:
    line = f.readlines()


# removing b'PR:
with open('temp.txt', 'a') as temporary:
    for each in line:
        each = re.sub(r"b'PR:",'',each)
        temporary.write(each)

import time
time.sleep(5)

# finally remove b' from the strings
fname = 'temp.txt'
with open(fname) as f:
    fLine = f.readlines()



with open('final.csv', 'a') as ready:
    for each in fLine:
        each = re.sub(r"b'",'',each)
        ready.write(each.lower())