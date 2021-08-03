import pandas as pd
from sklearn.tree import DecisionTreeClassifier
music_data=pd.read_csv('music.csv')
X=music_data.drop(columns=["genre"]) #input data set
# print(X)
y=music_data['genre']
print(y)