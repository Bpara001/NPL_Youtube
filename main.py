import nltk
import random
import json
import re
import urllib.request
import googleapiclient.discovery
import googleapiclient.errors
from nltk.corpus import movie_reviews
import random
import sys
All_Comments = []
x = sys.argv[1]
PositiveComments = nltk.FreqDist(w.lower() for w in All_Comments)
word_feature = list(PositiveComments)[:2000]


def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_feature:
        features['contains ({})'.format(word)] = (word in document_words)
        return features


featuresets = [(document_features(d), c) for (d,c) in All_Comments]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)