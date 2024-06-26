# -*- coding: utf-8 -*-
"""TrainTestSplit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N5pAGpZ8vdTsckMz0sH0kcm8Yxqhp5ZU
"""

# Load libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, KFold

# Read in data set
df = pd.read_csv('/content/Medical_Insurance_Cost_Linear_Regression_Data.csv')
print(df.head())
print(df.shape)

# Filter to a sample of 100 claims for illustration visibility
data = df.sample(100)

# Create X and y features
X = data[['bmi']]
y = data['charges']

"""## Train-Test Split:
*   We split the dataset into training (80%) and test (20%) sets.
*   We visualize the training data in blue and the test data in green.





"""

# Train-Test Split Visualization
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

plt.figure(figsize=(18, 5))

plt.subplot(1, 3, 1)
plt.scatter(X_train, y_train, c='blue', label='Training Data', alpha=0.5)
plt.scatter(X_test, y_test, c='green', label='Test Data', alpha=0.5)
plt.title('Train-Test Split')
plt.legend()

"""## Train-Validation-Test Split:
*   We split the dataset into train+validation (80%) and test (20%) sets.
*   Further, we split the train+validation set into training (60%) and validation (20%) sets.
*   We visualize the training data in blue, validation data in orange, and test data in green.


"""

# Train-Validation-Test Split Visualization
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)


plt.scatter(X_train, y_train, c='blue', label='Training Data', alpha = 0.5)
plt.scatter(X_val, y_val, c='orange', label='Validation Data', alpha=0.5)
plt.scatter(X_test, y_test, c='green', label='Test Data', alpha=0.5)
plt.title('Train-Validation-Test Split')
plt.legend()

"""## Cross-Validation (5-Fold):
*   We perform 5-fold cross-validation.
*   We visualize each fold with a different color using seaborn's color palette.
*   Training samples for each fold are shown with filled circles, and validation samples for each fold are shown with edge-colored circles.





"""

# Create X and y features
X = data[['bmi']].values  # Ensure X is a numpy array
y = data['charges'].values  # Ensure y is a numpy array

# Cross-Validation Visualization
kf = KFold(n_splits=5, shuffle=True, random_state=42)
fold_colors = sns.color_palette('husl', 5)

plt.figure(figsize=(15, 10))
for fold, (train_index, test_index) in enumerate(kf.split(X)):
    plt.subplot(3, 2, fold + 1)
    plt.scatter(X[train_index], y[train_index], c='blue', label='Training Data', alpha=0.5)
    plt.scatter(X[test_index], y[test_index], c='orange', edgecolor='k', label='Validation Data', alpha=0.5)
    plt.title(f'Fold {fold+1}')
    if fold == 0:
        plt.legend()

plt.tight_layout()
plt.show()

