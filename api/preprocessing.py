import nltk
nltk.download('stopwords')
from nltk.corpus import names, stopwords, words
stopword = sorted(stopwords.words('english'))
print(stopword)

