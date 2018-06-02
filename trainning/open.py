import pandas as pd
from nltk.corpus import stopwords
import numpy as np

import nltk
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

result = pd.read_csv("output.csv",header=0,\
                    delimiter=",", quoting=3)

test1 = pd.read_csv("labeledTrainData.tsv",header=0,\
                    delimiter="\t", quoting=3)
# test = test1[0:5000]

testSentiment = test["sentiment"]
resultSentiment = result["sentiment"]


print(test[(test['id']==result['id'])&(test['sentiment']==result['sentiment'])])

# print(test.set_index(['id'])-result.set_index(['id']))
    

# print (test["5814_8"])
# print(result)
# print(result)
# print(testSentiment[1],resultSentiment[1])

# print(test["sentiment"])
