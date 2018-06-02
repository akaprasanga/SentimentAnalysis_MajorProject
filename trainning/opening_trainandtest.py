import pandas as pd

test = pd.read_csv("testTweet.csv",header=0,\
                    delimiter="\t", quoting=3)

result = pd.read_csv("output.csv",header=0,\
                    delimiter="\t", quoting=3)
test1 = test['sentiment']


print(test)
print((test.sentiment == result.sentiment).value_counts())

# print("----------------------predicted--------------------")
# # print(result)
# # print(test)
# # print(test['review'])
# print("----------------------original--------------------")

# # print(test1)