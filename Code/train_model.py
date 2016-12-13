# %load train_model.py
'''
train_model.py
@author: jubinsoni
Text analysis
'''

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import re, csv, sys

reload(sys)
sys.setdefaultencoding('utf8')


def createDict(calorie_file):
    calorie = pd.read_csv(calorie_file)
    d = {}
    i = 0
    for foodsubcategory in calorie.FoodSubcategory:
        d[foodsubcategory.lower()] = calorie.Calories[i]
        i = i + 1
    return d


def search(d, searchFor):
    df = pd.DataFrame({'food': d.keys(), 'calorie': d.values()})
    return df[df['food'].str.contains(searchFor)]


def getActualValue(searchFor):
    d = createDict(calorie_file='calorie_dataset.csv')
    a = search(d,searchFor.lower())
    return np.array([a.values[0][0]])


def train_calorie_model(data_file):
    train = pd.read_csv(data_file)
    vectorizer = TfidfVectorizer(min_df=1, ngram_range=(1, 10))
    X_train = vectorizer.fit_transform(np.array(train.Food))
    model = MultinomialNB().fit(X_train, np.array(train.Calories))
    return model, vectorizer


def get_score_of_calorie(text):
    actual = getActualValue(text)
    predicted = float(get_calorie(text)[0])
    #accuracy_score = metrics.accuracy_score(predicted,actual)
    accuracy_score = predicted/actual
    return accuracy_score


def get_calorie(text):
    data_file = 'calorie_dataset.csv'
    model, vectorizer = train_calorie_model(data_file)
    test = vectorizer.transform([text])
    return model.predict(test)


if __name__ == '__main__':
    food = "Apple" #Pizza, Stawberry, Burger, Fries, Biriyani, Dosa, Egg, etc...
    d = createDict(calorie_file='calorie_dataset.csv')
    print food,"has %s calories." % get_calorie(food.lower())
    print "Accuracy Score: %f" % get_score_of_calorie(food.lower())
    print "Other healthy options: \n %s" % (search(d, food.lower()))
    #print getActualValue(food)
