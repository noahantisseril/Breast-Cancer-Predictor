import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.model_selection import train_test_split


data = pd.read_csv("data.csv")
X = data[['age', 'menopause', 'tumor.size', 'inv.nodes', 'node.caps', 'deg.malig', 'breast', 'irradiat']]
y = data['Class']
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.15, random_state=49)


model = RandomForestClassifier().fit(X_train, y_train)
averageAccuracy = 0.0
for i in range(100):
    fit = RandomForestClassifier().fit(X_train, y_train)
    y_pred = fit.predict(X_test)
    averageAccuracy = averageAccuracy + float(accuracy_score(y_test, y_pred))
averageAccuracy = averageAccuracy / 100

#User Interface
check = True;
while(check) :
    x = []
    x.append(int(input("Enter your age. (0 = 20-29, 1 = 30-39, 2 = 40-49, 3 = 59-59, 4 = 60-69, 5 = 70-79)\n")))
    x.append(int(input("Enter your stage of menopause. (0 = premenopause, 1 = ge40, 2 = lt40)\n")))
    x.append(int(input("Enter your tumor size. (0 = 0-4, 1 = 5-9, 2 = 10-14, 3 = 15-19, 4 = 20-24, 5 = 25-29, 6 = 30-34, 7 = 35-39, 8 = 40-44, 9 = 45-49, 10 = 50-54)\n")))
    x.append(int(input("Enter the number of axillary lymph nodes. (0 = 0-2, 1 = 3-5, 2 = 6-8, 3 = 9-11, 4 = 12-14, 5 = 15-17, 6 = 18-20, 7 = 21-23, 8 = 24-26)\n")))
    x.append(int(input("Enter if you have node caps or not. (0 = Yes, 1 = No)\n")))
    x.append(int(input("Enter your degree of malignancy. (1 = normal, 2 = benign, 3 = malignant)\n")))
    x.append(int(input("Enter which breast it occured in. (0 = right, 1 = left)\n")))
    x.append(int(input("Enter if radiation was used as therapy. (0 = yes, 1 = no)\n")))
    print("\n")
    print("Calculating result...\n")
    x = np.reshape(x, (1, -1))
    prediction = model.predict(x)
    
    if(prediction[0] == 0):
        print("We can say with" + str(averageAccuracy) + " percent accuracy that you will have a recurrance of breast cancer.") 
    else:
        print("We can say with " + str(averageAccuracy) + " percent accuracy that you will not have a recurrance of breast cancer.") 
        
    y = (int(input("Would you like to run the program again? (0 = Yes, 1 = No)\n")))
    if y==1:
        check=False
