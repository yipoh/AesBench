import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# >> Load two CSV files:
ground_truth_df = pd.read_csv('../data_release/ground_truth.csv')
prediction_df = pd.read_csv('../data_release/prediction_AesA1.csv')

# Merge the dataframes on the 'Image Name' column
merged_df = pd.merge(ground_truth_df, prediction_df, on='Image Name')

# Remove any leading or trailing spaces in the column names
merged_df.columns = merged_df.columns.str.strip()

# Extract the ground truth and predicted values
y_true = merged_df['AesA1_Score']  # Ground truth (actual) values
y_pred = merged_df['Aesthetic Response']  # Predicted values

# Calculate the confusion matrix
cm = confusion_matrix(y_true, y_pred, labels=["High", "Medium", "Low"])

# Create a confusion matrix heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["High", "Medium", "Low"], yticklabels=["High", "Medium", "Low"])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix for AesA1_Score')
plt.show()