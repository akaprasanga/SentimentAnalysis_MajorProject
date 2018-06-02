import re
from random import shuffle

# create a empty temporary file
final = open("lower.csv",'a').close()


fname = 'final.csv'
with open(fname) as f:
    line = f.readlines()
    for all in line:
        each_sent  = all.lower()
        print (each_sent)
        with open('lower.csv', 'a') as temporary:
            temporary.write(each_sent)

