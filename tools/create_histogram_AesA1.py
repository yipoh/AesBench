import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files 
ground_truth_df = pd.read_csv('../data_release/ground_truth.csv')
predicted_df = pd.read_csv('../data_release/prediction_AesA1.csv')

# Select the column
ground_truth_classification = ground_truth_df['AesA1_Score']
predicted_classification = predicted_df['Aesthetic Response']

# Count the occurrences of each category in both datasets
ground_truth_counts = ground_truth_classification.value_counts()
predicted_counts = predicted_classification.value_counts()

# Create a bar chart
fig, ax = plt.subplots(figsize=(8, 6))

# Set a modern style
plt.style.use('ggplot')

# Plot for ground truth classification
ax.bar(ground_truth_counts.index, ground_truth_counts.values, alpha=0.6, label='Ground Truth', color='#1f77b4')

# Plot for predicted classification
ax.bar(predicted_counts.index, predicted_counts.values, alpha=0.6, label='Predicted', color='#ff7f0e')

# Add labels and title
plt.xlabel('Classification (High, Medium, Low)', fontsize=12)
plt.ylabel('Number of Images', fontsize=12)
plt.title('Comparison of Ground Truth and Predicted Classifications', fontsize=14)

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()