import pandas as pd
import nltk
import gensim
from gensim.models import Word2Vec
from gensim import corpora, models, similarities

# model = gensim.models.Word2Vec.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)  

# df=pd.read_csv('lower.csv')


# x=df['tweets'].values.tolist()


# corpus = x
  
# tok_corp= [nltk.word_tokenize(sent) for sent in corpus]


# model = gensim.models.Word2Vec(tok_corp, window=3, min_count=1, size = 500)

# model.save('test2')

model  = Word2Vec.load('test2')
# model = gensim.models.Word2Vec.load('test.bin')
print(model)

similar = model.most_similar('cryptocurrency')
print(similar)

# print(dad.shape)
# print(dad[:10])
#model.most_similar([vector])