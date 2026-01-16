import csv

# Read existing CSV
input_file = 'data.csv'
output_file = 'data_updated.csv'

rows_updated = []

with open(input_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    old_fieldnames = reader.fieldnames
    
    # Add 'Webpage' column if it doesn't exist
    new_fieldnames = list(old_fieldnames)
    if 'Webpage' not in new_fieldnames:
        new_fieldnames.append('Webpage')
        print("✅ Added 'Webpage' column to CSV")
    
    for row in reader:
        # Add webpage link for Hari Tech Solutions
        if row['Name'].strip() == 'Hari Tech Solutions' and row['Category'].strip() == 'Website Designers':
            row['Webpage'] = 'haritech.html'
            print(f"✅ Added webpage link for Hari Tech Solutions: haritech.html")
        elif 'Webpage' not in row:
            row['Webpage'] = ''
        
        rows_updated.append(row)

# Write updated data with new column
with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=new_fieldnames)
    writer.writeheader()
    writer.writerows(rows_updated)

# Replace original file
import shutil
shutil.move(output_file, input_file)

print(f"✅ Updated CSV with Webpage column")
