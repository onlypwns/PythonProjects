import numpy as np
import pandas as pd
import os
import matplotlib 

df = pd.read_csv('data'+os.sep +'iris.csv')
df.head()

df = df.drop(columns=['Id'])

X = df.iloc[:, :-1]
y = df.iloc[:, -1]
print(X.shape)
print(y.shape)
print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

from sklearn.linear_model import SGDClassifier

model = SGDClassifier()

model.fit(X_train, y_train)
pred = model.predict(X_test)

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
print(accuracy_score(pred, y_test))
print(precision_score(pred, y_test, average ='macro'))
print(recall_score(pred, y_test, average ='macro'))
print(f1_score(pred, y_test, average ='macro'))

model = SGDClassifier(loss='log')

model.fit(X_train,y_train)
pred = model.predict(X_test)

accuracy_score(pred, y_test)

from sklearn.model_selection import cross_val_score
cross_val_score(model,X_train,y_train,cv=5,scoring='accuracy')


print(precision_score(pred, y_test,average='macro'))
print(recall_score(pred, y_test,average='macro'))
print(f1_score(pred, y_test,average='macro'))

from sklearn.metrics import confusion_matrix
print(y_test)
confusion_matrix(pred,y_test)


