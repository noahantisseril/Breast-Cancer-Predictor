import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier




data = pd.read_csv("data.csv")
X = data[['age', 'menopause', 'tumor.size', 'inv.nodes', 'node.caps', 'deg.malig', 'breast', 'irradiat']]
y = data['Class']
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.15, random_state=42)

def test_model(model):
    fit = model.fit(X_train, y_train)
    y_pred = fit.predict(X_test)
    confusionMatrix = confusion_matrix(y_test, y_pred, labels=fit.classes_)
    display = ConfusionMatrixDisplay(confusion_matrix=confusionMatrix, display_labels=fit.classes_)
    display.plot()
    plt.show()
    print(str(model) + ' Accuracy Score: ' + str(accuracy_score(y_test, y_pred)))
    print(str(model) + ' f1 Score: ' + str(f1_score(y_test, y_pred, average=None, zero_division=0)))


#Trained multiple models to determine accuracy - Decided on a Random Forest Classifier
models = [LinearSVC(), DecisionTreeClassifier(),LogisticRegression(), KNeighborsClassifier(), GaussianNB(), RandomForestClassifier()]
average=0.0
f1=0.0
for model in models:
    average=0.0
    for i in range(100):
        fit = model.fit(X_train, y_train)
        y_pred = fit.predict(X_test)
        confusionMatrix = confusion_matrix(y_test, y_pred, labels=fit.classes_)
        average=average+float(accuracy_score(y_test, y_pred))
    print(str(model)+"   "+str(average/100))
        

model=RandomForestClassifier().fit(X_train, y_train)
#User Interface
check=False;
while(check) :
    x = []
    x.append(int(input("Enter your age. (0 = 20-29, 1 = 30-39, 2 = 40-49, 3 = 59-59, 4 = 60-69, 5 = 70-79)\n")))
    x.append(int(input("Enter your menopause stage. (0 = premenopause, 1 = ge40, 2 = lt40)\n")))
    x.append(int(input("Enter your tumor size. (0 = 0-4, 1 = 5-9, 2 = 10-14, 3 = 15-19, 4 = 20-24, 5 = 25-29, 6 = 30-34, 7 = 35-39, 8 = 40-44, 9 = 45-49, 10 = 50-54)\n")))
    x.append(int(input("Enter the number of axillary lymph nodes. (0 = 0-2, 1 = 3-5, 2 = 6-8, 3 = 9-11, 4 = 12-14, 5 = 15-17, 6 = 18-20, 7 = 21-23, 8 = 24-26)\n")))
    x.append(int(input("Enter if you have node caps or not. (0 = Yes, 1 = No)\n")))
    x.append(int(input("Enter your degree of malignancy. (1 = normal, 2 = benign, 3 = malignant)\n")))
    x.append(int(input("Enter which breast it occured in. (0 = right, 1 = left)\n")))
    x.append(int(input("Enter if radiation was used as ther3apy. (0 = yes, 1 = no)\n")))
    print("\n")
    print("Calculating result...\n")
    x = np.reshape(x, (1, -1))
    prediction = model.predict(x)
    
    if(prediction[0] == 0):
        print("We can say with 78.66 percent accuracy that you will have a recurrance of breast cancer.") 
    else:
        print("We can say with 78.66 percent accuracy that you will not have a recurrance of breast cancer.") 
        
    y = (int(input("Would you like to run the program again? (0 = Yes, 1 = No)\n")))
    if y==1:
        check=False
