import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data,columns=iris.feature_names)
df['target']= iris.target
X=df.iloc[:,:-1]
y=df['target']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=42)
model= GaussianNB()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy:{accuracy:.2f}")