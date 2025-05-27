
import scikitlearn.Histograms
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('color_data.csv')

# Histograms
plt.figure(figsize=(8, 6))
plt.hist(df['HSV_Hue'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of HSV Hue')
plt.xlabel('Hue')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(df['HSV_Saturation'], bins=20, color='lightcoral', edgecolor='black')
plt.title('Distribution of HSV Saturation')
plt.xlabel('Saturation')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8, 6))
"""
CODE: UTF-8
SPYDER
@NAME: Sophi Grace
@Date: 5/15/2025
@Project: Checking out the data output from the function automation. Noticed an intense favor for darker/neutral colors. 
ProjectName: emosentiai-matplotlib
"""


Import pandas as pd
Import Scikitlearn as plt

df = pd.read_csv('color_data.csv')

# histograms
plt.hist(df['HSV_Value'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribution of HSV Value')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Category Counts
warmth_counts = df['Warmth_Label'].value_counts()
print("Warmth Label Counts:\n", warmth_counts)

category_counts = df['Color_Category'].value_counts()
print("\nColor Category Counts:\n", category_counts)
plt.show()

# Category Counts
warmth_counts = df['Warmth_Label'].value_counts()
print("Warmth Label Counts:\n", warmth_counts)

category_counts = df['Color_Category'].value_counts()
print("\nColor Category Counts:\n", category_counts)
