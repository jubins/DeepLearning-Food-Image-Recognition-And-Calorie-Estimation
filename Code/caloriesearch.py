import pandas as pd

def createDict(calorie_file):
    calorie = pd.read_csv(calorie_file)
    d = {}
    i=0
    for foodsubcategory in calorie.FoodSubcategory:
        d[foodsubcategory.lower()] = calorie.Calories[i]
        i = i+1
    return d

def search(d,searchFor):
    df = pd.DataFrame({'food': d.keys(), 'calorie': d.values()})
    return df[df['food'].str.contains(searchFor)]

d=createDict(calorie_file = 'calorie_dataset.csv')

searchFor = "pizza" #Checks if string 'cheese' exists in dictionary value
#prints food, calorie
print search(d, searchFor)