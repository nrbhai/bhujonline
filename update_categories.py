import csv

# Read the CSV file
input_file = 'data.csv'
output_file = 'data_updated.csv'

rows_updated = []

with open(input_file, 'r', encoding='latin-1') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    
    for row in reader:
        category = row['Category'].strip()
        
        # Change "AC/Fridge Repair" to "Ac fridge repairer"
        if category == 'AC/Fridge Repair':
            row['Category'] = 'Ac fridge repairer'
            print(f"Merged: {row['Name']} from AC/Fridge Repair -> Ac fridge repairer")
        
        # Rename "Computer Laptop repairs" to "Computer Laptop Sales"
        elif category == 'Computer Laptop repairs':
            row['Category'] = 'Computer Laptop Sales'
            print(f"Renamed category for: {row['Name']} -> Computer Laptop Sales")
        
        rows_updated.append(row)

# Write updated data
with open(output_file, 'w', encoding='latin-1', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_updated)

# Replace original file
import shutil
shutil.move(output_file, input_file)

print(f"\n✅ Merged AC/Fridge Repair -> Ac fridge repairer")
print(f"✅ Renamed Computer Laptop repairs -> Computer Laptop Sales")
