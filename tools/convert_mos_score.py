"""
Description: This code is to create new ground truth from the orginal ground truth
             by converting the high-medium-low to its equivalent numerical scores.
             Original ground truth only have high-medium-low value for each image,
             new ground truth will have both high-medium-low and numerical scores.
"""
import pandas as pd

# Load the CSV file from the specified location
mos_df = pd.read_csv('../data_release/original_ground_truth.csv')

# Define the function to categorize MOS
def categorize_mos(mos):
    if mos < 0.33:
        return 'Low'
    elif mos <= 0.66:
        return 'Medium'
    else:
        return 'High'

# Apply the transformations with relevant rules
mos_df['AesA3_Score'] = (1 + 9 * mos_df['MOS']).round(0).astype(int)  # Scale 1-10
mos_df['AesA2_Score'] = (1 + 4 * mos_df['MOS']).round(0).astype(int)  # Scale 1-5 
mos_df['AesA1_Score'] = mos_df['MOS'].apply(categorize_mos)           # Categorisation

# Save the updated dataframe to the specified location
mos_df.to_csv('../data_release/new_ground_truth.csv', index=False)