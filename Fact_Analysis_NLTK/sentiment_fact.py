import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
from openpyxl import load_workbook
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string
import xlwt

import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
read_data = pd.read_excel('A.xls', index=False)
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []
for i in range(31):
    reviews = re.sub(r'[^a-zA-Z]', ' ', read_data['Contents'][i])
    reviews = reviews.lower()
    reviews = reviews.split()
    ps = PorterStemmer()
    reviews = [ps.stem(word) for word in reviews if not word in set(stopwords.words('english'))]
    reviews = ' '.join(reviews)
    corpus.append(reviews)

print(corpus)


def findpolar(test_data):
    sia = SentimentIntensityAnalyzer()

    polarity = sia.polarity_scores(test_data)["compound"]
    if polarity >= 0.1:
        # foundpolar = 1
        foundpolar = "Positive"
        return foundpolar
    if (polarity <= -0.1):
        # foundpolar = -1
        foundpolar = "Negative"
        return foundpolar
    if (polarity >= -0.1 and polarity <= 0.1):
        # foundpolar = 0
        foundpolar = "Positive"
        return foundpolar


read_data['sentiment'] = '';
for s in range(31):
    sentiment = findpolar(corpus[s])  # type: int
    print(sentiment)
    read_data['sentiment'][s] = sentiment

"""
Thsi is for finding most discussed Topic/facts
"""

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english', max_features=500,
                             max_df=0.5,
                             smooth_idf=True)

X = vectorizer.fit_transform(read_data["Contents"])

print(X)
print(X.shape)

from sklearn.decomposition import TruncatedSVD

theme1 = []
theme2 = []
for i in range(63):
    # SVD represent documents and terms in vectors

    svd_model = TruncatedSVD(n_components=1, algorithm='randomized', n_iter=100, random_state=122)

    svd_model.fit(X[i])

    print(len(svd_model.components_))

    terms = vectorizer.get_feature_names()

    for i, comp in enumerate(svd_model.components_):
        terms_comp = zip(terms, comp)
        sorted_terms = sorted(terms_comp, key=lambda x: x[1], reverse=True)[:2]

        cnt = 0
        for t in sorted_terms:
            if cnt == 0:
                theme1.append(t[0])
                cnt += 1
            else:
                theme2.append(t[0])
                cnt += 1

read_data['Theme 1'] = theme1;
read_data['Theme 2'] = theme2;

read_data.to_excel("A_final.xls", index=False)




