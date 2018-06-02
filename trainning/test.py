import pandas as pd
from nltk.corpus import stopwords
import numpy as np

import nltk
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import pprint

train = pd.read_csv("labeledTweet.csv",header=0,\
                    delimiter="\t", quoting=3)

test = pd.read_csv("testTweet.csv",header=0,\
                    delimiter="\t", quoting=3)



# print(test)
# print(train)

def review_wordlist(review , remove_stopwords=False):

    review_text  = BeautifulSoup(review).get_text()
    review_text  = re.sub("[^a-zA-Z]"," ",review_text)
    words = review_text.lower().split()

    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words  = [w for w in words if not w in stops]
        
    return(words)





def review_sentences(review, tokenizer, remove_stopwords=False):

    raw_sentences = tokenizer.tokenize(review.strip())
    sentences = []

    for raw_sentence in raw_sentences:
        if len(raw_sentence)>0:
            sentences.append(review_wordlist(raw_sentence,remove_stopwords))
    return sentences

sentences = []

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

print("parsing sentences from training set")


for review in train["review"]:
    sentences += review_sentences(review,tokenizer)



# Importing the built-in logging module
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)




# Creating the model and setting values for the various parameters
num_features = 500  # Word vector dimensionality
min_word_count = 40 # Minimum word count
num_workers = 4     # Number of parallel threads
context = 10        # Context window size
downsampling = 1e-3 # (0.001) Downsample setting for frequent words

# # Initializing the train model
from gensim.models import word2vec
# print("Training model....")
# model = word2vec.Word2Vec(sentences,\
#                           workers=num_workers,\
#                           size=num_features,\
#                           min_count=min_word_count,\
#                           window=context,
#                           sample=downsampling)

# # To make the model memory efficient
# model.init_sims(replace=True)

# Saving the model for later use. Can be loaded using Word2Vec.load()
model_name = "300features_40minwords_10context"
model = word2vec.Word2VecKeyedVectors.load(model_name)

# print(model["man"])
# Function to average all word vectors in a paragraph

def featureVecMethod(words, model, num_features):
    # intializing new zero vector
    featureVec = np.zeros(num_features,dtype = 'float32')
    nwords = 0

#Converting Index2Word which is a list of words only to a set for better speed in the execution.
    index2word_set = set(model.wv.index2word)

    for word in words:
        if word in index2word_set:
            nwords = nwords + 1
            featureVec = np.add(featureVec,model[word])

    featureVec = np.divide(featureVec,nwords)
    return featureVec



# Function for calculating the average feature vector
def getAvgFeatureVec(reviews, model,num_features):
    counter = 0
    reviewFeatureVecs = np.zeros((len(reviews),num_features),dtype = 'float32')

    for review in reviews:
        # Printing a status message every 1000th review
        if counter%100 == 0:
            print("Review %d of %d"%(counter,len(reviews)))
        reviewFeatureVecs[counter] = featureVecMethod(review,model,num_features)
        counter = counter+1
    return reviewFeatureVecs

# Calculating average feature vector for training set
clean_train_reviews = []
for review in train['review']:
    clean_train_reviews.append(review_wordlist(review, remove_stopwords=True))
    
trainDataVecs = getAvgFeatureVec(clean_train_reviews, model, num_features)

# Calculating average feature vactors for test set     
clean_test_reviews = []
for review in test["review"]:
    clean_test_reviews.append(review_wordlist(review,remove_stopwords=True))
    
testDataVecs = getAvgFeatureVec(clean_test_reviews, model, num_features)

from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators = 100)
    
print("Fitting random forest to training data....")    
forest = forest.fit(trainDataVecs, train["sentiment"])

print("Predicting the test data")
result = forest.predict(testDataVecs)
output = pd.DataFrame(data={"sentiment":result})

print('Parameters currently in use:\n')
pprint.pprint(forest.get_params())

# test_labels = test["sentiment"]
# errors = abs(result - test_labels)
# mape = 100 * np.mean(errors / test_labels)
# accuracy = 100 - mape
# print('Model Performance')
# print('Average Error: {:0.4f} degrees.'.format(np.mean(errors)))
# print('Accuracy = {:0.2f}%.'.format(accuracy))

output.to_csv( "output.csv", index=False, quoting=3 )

counter = 0

# finalResult = pd.read_csv("output.csv",header=0,\
#                     delimiter="\t", quoting=3)
