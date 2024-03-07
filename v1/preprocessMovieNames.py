import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

import nltk
nltk.download('punkt')
nltk.download('stopwords')

df = pd.read_csv('cleanedMovieTitles.csv')

def preprocess(text):
    text = text.lower()
    text =text.translate(str.maketrans("","",string.punctuation))
    
    tokens = word_tokenize(text)
    
    stopWords = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stopWords]

    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return "".join(tokens)

df['processedTitle'] = df['title'].apply(preprocess)

print(df['processedTitle'].head())

df.to_csv('processedMovieNames.csv')
