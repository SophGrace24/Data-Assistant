# -*- coding:UTF-8 -*-
"""
Created on Sun May 11 07:45:35 2025
@author: sophgrace24
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow
from tensorflow.keras import models, layers
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential as Seq


df = pd.read_csv("Version_ONE_FullAssociations - colorwarmth.csv")

# Extract RGB Values


def extract_rgb(rgb_string):  # Function defined HERE, BEFORE it's used
    """
    Extracts the R, G, and B values from a string in the format "R, G, B".
    Returns a NumPy array of floats [R, G, B] scaled to the range 0-1.
    """
    try:
        rgb_values = rgb_string.split(',')
        r = float(rgb_values[0].strip()) / 255.0
        g = float(rgb_values[1].strip()) / 255.0
        b = float(rgb_values[2].strip()) / 255.0
        return np.array([r, g, b])
    except:
        return np.array([0.0, 0.0, 0.0])  # Handle potential errors


# Function used HERE, OUTSIDE the function definition
df['RGB'] = df['RGB_ID'].apply(extract_rgb)


# prepare data for training and validation

X = np.array(df['RGB'].tolist())  # features: rgb values
y = np.array(df['WARM'])  # target: warmth 0 or 1

# SPLIT the data into training/validation

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.6, random_state=12)

# 80% training, 20% validation

# DEFINE THE MODEL

model = tensorflow.keras.Sequential()
model.add(Dense(29, activation="relu", input_shape=(3,)))
model.add(Dense(1, activation="sigmoid"))

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model.fit(X_train, y_train, epochs=40)

loss, accuracy = model.evaluate(X_val, y_val, verbose=0)
print("Loss: ", loss)
print("Accuracy: ", accuracy)


'''
print("\n--- DATA SPLITTING ---")
print("Shape of x.train: ", X_train.shape)
print("Shape of X.val: ", X_val.shape)
print("Shape of Y train and Y val: ", y_train.shape, y_val.shape)
'''
