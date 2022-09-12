# Breast-Cancer-Predictor

We created a Random Forest model to predict whether someone would have a recurrence of breast cancer based on parameters including age, node count, and if radiation was used. To optimize the class of the model and the model itself, we varied the n-estimators, tree depth, maximum features, random state, and model type. After 100 trials with each model, the following accuracy values were discovered:

        LinearSVC : 80.95% 

        DecisionTreeClassifier: 76.88%

        LogisticRegression: 83.33%

        KNeighborsClassifier: 76.19%

        GaussianNB: 76.19%

        RandomForestClassifier: 86.49%

We ultimately settled on a RandomForestClassifier model with a **67% True Positive Rate** and a **94% True Negative Rate**.
