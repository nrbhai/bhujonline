import csv

# Read the CSV file
input_file = 'data.csv'
output_file = 'data_updated.csv'

rows_updated = []

with open(input_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    
    for row in reader:
        # Add webpage link for Pioneer Computer Services
        if 'Pioneer Computer' in row['Name'] and 'Computer' in row['Category']:
            row['Webpage'] = 'pioneer.html'
            print(f"✅ Added webpage link for {row['Name']}: pioneer.html")
        
        rows_updated.append(row)

# Write updated data
with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_updated)

# Replace original file
import shutil
shutil.move(output_file, input_file)

print(f"✅ Updated CSV with Pioneer Computer webpage link")
