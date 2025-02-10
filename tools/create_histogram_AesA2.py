import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
ground_truth_df = pd.read_csv('../data_release/ground_truth.csv')
predicted_df = pd.read_csv('../data_release/prediction_AesA2.csv')

# Assuming both CSVs have columns 'image_name' and 'score'
ground_truth_scores = ground_truth_df['AesA2_Score']
predicted_scores = predicted_df['Aesthetic Response']

# Set a modern style
plt.style.use('ggplot')

# Create a figure for the histograms
plt.figure(figsize=(10, 6))

# Plot histogram for ground truth scores
plt.hist(ground_truth_scores, bins=[1, 2, 3, 4, 5, 6], alpha=0.6, label='Ground Truth', color='#1f77b4', edgecolor='black', align='left')

# Plot histogram for predicted scores
plt.hist(predicted_scores, bins=[1, 2, 3, 4, 5, 6], alpha=0.6, label='Predicted Scores', color='#ff7f0e', edgecolor='black', align='left')

# Add labels and title
plt.xlabel('Aesthetic Score (1-5)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('AesA2 Numerical Comparison of Ground Truth and Predicted Scores', fontsize=14)

# Add grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add legend without frame
plt.legend(frameon=False, fontsize=10)

# Set x-ticks to show values from 1 to 5
plt.xticks([1, 2, 3, 4, 5], fontsize=10)

# Adjust ticks
plt.yticks(fontsize=10)

# Show the plot
plt.tight_layout()
plt.show()