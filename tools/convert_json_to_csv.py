# Convert result_n.json --> prediction_AesAn.csv
# Goal is to use the obtained file for confussion matrix

import json
import csv

# >> Locate paths:
json_path = '../history/AesA3/test1.json'             # Choose json result history of gpt responses
csv_path = '../data_release/prediction_AesA3.csv'     # Choose csv output file path


def convert_json_to_csv(json_path, csv_path):
    # Read JSON data from file
    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Prepare data for CSV
    # >> Locate AesA response number:
    csv_data = []
    for image_name, details in json_data.items():
        # Extract the "Answer" part
        aes_response = details['AesA3_response'].split('\n')[0].split(': ')[1]
        csv_data.append([image_name, aes_response])

    # Write to CSV
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Image Name", "Aesthetic Response"])
        writer.writerows(csv_data)

    print(f"Data has been converted and written to {csv_path}")

convert_json_to_csv(json_path, csv_path)