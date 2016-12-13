import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn import svm
import seaborn
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline
#Load target
food_file = "food.csv"
cuisine = pd.read_csv(food_file)
target = {}
i = 0
for cuisineName in cuisine.Cuisine:
    target[cuisineName.lower()] = cuisine.CuisineNumber[i]
    i += 1
    
#Load features
categories = pd.read_csv(food_file)
features_category = {}
i = 0
for category in categories.FoodName:
    features_category[category.lower()] = []
    features_category[category.lower()].append(categories.FoodNumber[i])
    features_category[category.lower()].append(categories.Price[i])
    i += 1
feature = []

for category in categories.FoodName:
    feature.append(features_category[category.lower()])
    
features = np.array(feature)
X, y = features, target.keys()
model = KMeans(n_clusters=12)
model.fit(X)
#print model.cluster_centers_
dictLabels = {0:"american", 1:"african", 2:"chinese", 3:"ethiopian", 4:"indian",5:"italian",6:"fruit",7:"mandarin", 8:"mexican", 9:"mediterranean", 10:"thai", 11:"vietnamese"}


#Enter calorie value
predictCuisine = [19.6,7.9]
print "KMeans predicted cuisine as '%s'." %dictLabels[model.predict(predictCuisine)[0]]

print "Accuracy Score: %d" %model.score(X)

distortions = []
for i in range(1, 13):
    km = KMeans(n_clusters = i, 
               init='k-means++', 
               n_init=10, 
               max_iter=300, 
               random_state=0)
    km.fit(X)
    distortions.append(km.inertia_)
plt.plot(range(1,13), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()