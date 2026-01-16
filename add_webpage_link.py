import csv

# Read the CSV file
input_file = 'data.csv'
output_file = 'data_updated.csv'

rows_updated = []

with open(input_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    
    for row in reader:
        # Add webpage URL for Hari Tech Solutions
        if row['Name'].strip() == 'Hari Tech Solutions' and row['Category'].strip() == 'Website Designers':
            row['Tags'] = 'haritech.html'  # Using Tags field to store webpage URL
            print(f"✅ Added webpage link for Hari Tech Solutions: haritech.html")
        
        rows_updated.append(row)

# Write updated data
with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_updated)

# Replace original file
import shutil
shutil.move(output_file, input_file)

print(f"✅ Updated data.csv with webpage link")
