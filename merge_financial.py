import csv

# Read the CSV file
input_file = 'data.csv'
output_file = 'data_cleaned.csv'

rows_updated = []

with open(input_file, 'r', encoding='latin-1') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    
    for row in reader:
        # Merge "Financial advisor" to "Financial Advisors"
        if row['Category'].strip().lower() == 'financial advisor':
            row['Category'] = 'Financial Advisors'
            print(f"Merged: {row['Name']} -> Financial Advisors")
        
        rows_updated.append(row)

# Write cleaned data back
with open(output_file, 'w', encoding='latin-1', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_updated)

# Replace original file
import shutil
shutil.move(output_file, input_file)

print(f"✅ Merged Financial advisor -> Financial Advisors")
