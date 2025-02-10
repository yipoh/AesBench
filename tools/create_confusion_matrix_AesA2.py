import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Load the ground truth and prediction files using relative paths
ground_truth_df = pd.read_csv('../data_release/ground_truth.csv')
prediction_df = pd.read_csv('../data_release/prediction_AesA2.csv')

# Merge the dataframes on Image Name to align predictions with ground truth
merged_df = pd.merge(ground_truth_df, prediction_df, on='Image Name')

# Extract the true labels and predicted labels
y_true = merged_df['AesA2_Score']
y_pred = merged_df['Aesthetic Response']

# Get the unique labels from both true and predicted data
all_labels = sorted(list(set(y_true.unique()) | set(y_pred.unique())))

# Create the confusion matrix
cm = confusion_matrix(y_true, y_pred, labels=all_labels)

# Display the confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=all_labels)
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix for AesA2_Score')
plt.show()