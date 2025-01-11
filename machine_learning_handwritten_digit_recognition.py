# -*- coding: utf-8 -*-
"""Machine Learning: Handwritten Digit Recognition.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eQwsq0ZwqlNONtH7DmF7RAIIgVR2QtAU

Machine Learning: Handwritten Digit Recognition
"""

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
digits = load_digits()
X, y = digits.data, digits.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")