import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score

#Importing the dataset
df= pd.read_csv("./MachineLearning/Breast Cancer Detection/breast_cancer.csv")
X= df.iloc[:, 1:-1].values
y= df.iloc[:, -1].values

#Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2, random_state=0)

#Training the Logistic Regression model on the Training set
classifier= LogisticRegression(random_state= 0)
classifier.fit(X_train, y_train)

#Predicting the Test set results
y_pred= classifier.predict(X_test)

# Making the Confusion Matrix
cm= confusion_matrix(y_pred, y_test)

# Computing the accuracy with k-Fold Cross Validation
accuracies= cross_val_score(estimator= classifier, X= X_train, y=y_train, cv= 10)

#Printing all the Results
print("-="*15)
print(cm)
print(f"Accuracy: {accuracies.mean()*100:.2f}%")
print(f"Standard Deviation: {accuracies.std()*100:.2f}%")
print("-="*15)