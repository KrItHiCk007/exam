import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=50)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

for i in range(len(y_test)):
    if y_test[i] == y_pred[i]:
        print(f"Correct: Actual - {iris.target_names[y_test[i]]}, Predicted - {iris.target_names[y_pred[i]]}")
    else:
        print(f"Incorrect: Actual - {iris.target_names[y_test[i]]}, Predicted - {iris.target_names[y_pred[i]]}")