import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# from sklearn.externals.joblib import extjoblib
from sklearn import tree

#to save the models once it's trained to avoid loading model each time
music_data=pd.read_csv('music.csv')
X=music_data.drop(columns=["genre"]) #input data set
# print(X)
y=music_data['genre']
# print(y)

model=DecisionTreeClassifier()
model.fit(X,y)

# model=joblib.load('music_predictor.joblib')
tree.export_graphviz(model,out_file='music_recommendor.dot',feature_names=['age','gender'],
                     class_names=sorted(y.unique()),label='all',rounded=True,filled=True)

# predictions=model.predict([[21,1]])
# print(predictions)