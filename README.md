# Machine Preventive Maintenance Detector Classification Model
## Web Application
![Logo](https://github.com/Sohail00786/Machine-Preventive-Maintenance-Detector-Classification-Model/blob/aa8f6a2bb1b1fc79caad7189dc53bca2b0efb1b2/Application%20.gif)
## Problem Statement
- The problem is to reduce the cost due to unnecessary repairs by Classifying the Failure type faced by Machine so the user will have clear mind set how to deal with problem according to failure made by machine.
- So it is required to minimize the false predictions.

## Approach:

- The classical machine learning tasks like Data Exploration, Data Cleaning, Feature Engineering, Model Building and Model Testing. Try out different machine learning algorithms that’s best fit for the above case.

## Project Overview
- Its is Multiclass Classification model (One vs Rest Classifier)
- The system in focus to Classify Machine is facing failure or not for Maintenance purpose on Basis of Air Temparature, Process Temparature, Rotational Speed, Tool Wear, Torque produced by Machine.
##  Failure types that will get classified by model
1. Heat Dissipation Failure
2. Random Failures
3. Power Failure
4. Tool Wear Failure
5. Overstrain Failure
6. No failure if machine is not facing any failure
 ## The Model is Evaluted on basis of four Metrics
 - Precision
 - Recall
 - F1 Score
 - Confusion Matrix
 ## The Models Tried Out in this Project are
 1. Logistic Regression Classifier
 2. Decision Tree Classifier
 3. Random Forest Classifier
 4. XgBoost Classifier
 5. Ada Boost Classifier
 #### XgBoost Classifier Model Turned out to be best model with an accuracy of 99.4 %

## Setup
#### Step - 1 Install the Requirements
```bash
pip install -r requirements.txt
```

#### Step - 2 Run app.py file
```bash
python main.py
```

