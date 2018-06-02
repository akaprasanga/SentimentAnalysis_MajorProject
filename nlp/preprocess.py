from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
# from stemming.porter2 import stem

example_sent = "ORIGINAL SENTENCE = Markets Update: Cryptocurrency Prices Rebound But Uncertainty Still Lingers  #Bitcoin"
print(example_sent)

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

# filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []
ps = PorterStemmer()
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
        ww = ps.stem(w)
        # print(ww)


print(word_tokens)
print(filtered_sentence)