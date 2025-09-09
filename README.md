# Single Feature Logistic Regression

This repository contains a simple implementation of **logistic regression with one feature**, written from scratch using **NumPy**.  
The model is trained using **gradient descent**, and it can predict probabilities as well as classify inputs into two classes.

---

## 📖 Overview

- Logistic regression is a classification algorithm used to estimate the probability of a binary outcome (0 or 1).
- In this project:
  - We take a single feature `X` and corresponding labels `Y`.
  - Train a logistic regression model using **gradient descent**.
  - Minimize the **log loss (cross-entropy cost function)**.
  - Predict the probability of new inputs belonging to the positive class.
  - Classify based on a threshold of `0.5`.

---

## ⚙️ Features

- Logistic sigmoid function implementation
- Cross-entropy cost function
- Gradient descent optimization
- Prediction of probability & class
- Interactive input loop for testing the model

---

## 📂 Files

- `logistic_regression.py` → Main script containing:
  - Model initialization
  - Cost & gradient functions
  - Training loop
  - Prediction function

---

## 🧮 Example Run

```text
we have divided data into two classes, positive class and negative class
we will be predicting the probability of the given input being positive class
from the given data the transition almost occurs at x = 4.0
Enter a number: 3
the probability of input being in class 1 is : 0.27
since probability is less than 0.5 it is negative class
Enter 0 to predict more and 1 to exit :
```
---
## 📊 Mathematics

. Sigmoid Function: 
  
  hθ​(x)=1/(1+e−(θ0​+θ1​x)1​)
  
. Cost Function:
  
  J(θ)=−(1/m)*∑[y(i)log(hθ​(x(i)))+(1−y(i))log(1−hθ​(x(i)))] from i=1 to m 
  
. Gradient Descent Update Rule:
  
  θ:=θ−α⋅m1​XT(hθ​(X)−y)

