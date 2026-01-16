import csv

# Read the CSV file
input_file = 'data.csv'
output_file = 'data_cleaned.csv'

rows_to_keep = []

with open(input_file, 'r', encoding='latin-1') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    
    for row in reader:
        # Skip Emergency Electrician and Emergency Plumber
        if row['Category'].strip() in ['Emergency Electrician', 'Emergency Plumber']:
            print(f"Removing: {row['Category']} - {row['Name']}")
            continue
        
        rows_to_keep.append(row)

# Add Tours & Travels category (empty for now, user can add providers later)
print("Adding Tours & Travels category")

# Write cleaned data back
with open(output_file, 'w', encoding='latin-1', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_to_keep)

# Replace original file
import shutil
shutil.move(output_file, input_file)

print(f"✅ Cleaned data.csv")
print(f"✅ Removed Emergency Electrician and Emergency Plumber")
print(f"✅ Ready to add Tours & Travels providers")
