import numpy as np
import pandas as pd 
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
df = pd.read_csv("C:\\Users\\Tarunn\\Desktop\\Deployment\\joblib\\Cardio_vascular.csv")

print(df.head())

array = df.values
#print(array)

x = array[:,0:13] #all the rows and 12 columns i.e all independent variables
y = array[:,13] #all the rows and 13th varible i.e the target variable

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.20)
 
model = LogisticRegression()
model.fit(x_train,y_train)

y_pred_test = model.predict(x_test)

y_pred_train = model.predict(x_train)

train_accuracy = accuracy_score(y_pred_train,y_train)
print("Training Accuracy:",train_accuracy)
test_accuracy = accuracy_score(y_pred_test,y_test)
print("Training Accuracy:",test_accuracy)

#train_accuracy = model.score(x_train,y_train)
#print("Training Accuracy:",train_accuracy)
#test_accuracy = model.score(x_test,y_test)
#print("Training Accuracy:",test_accuracy)

joblib.dump(model,"Cardio_vascular.pkl") #saving the model
