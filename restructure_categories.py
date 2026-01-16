#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bhuj Online - Category Restructuring Script
Merges duplicates, removes unwanted categories, adds missing ones
"""

import json
import re
import shutil
from datetime import datetime

# Backup original file
backup_file = f"assets/js/data.js.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
shutil.copy2("assets/js/data.js", backup_file)
print(f"✓ Backup created: {backup_file}")

# Read the current data.js
with open("assets/js/data.js", "r", encoding="utf-8") as f:
    content = f.read()

# Extract the data array
match = re.search(r'window\.bhujData = (\[.*?\]);', content, re.DOTALL)
if not match:
    print("ERROR: Could not find bhujData array")
    exit(1)

data_array = json.loads(match.group(1))
print(f"✓ Loaded {len(data_array)} existing categories")

# Create a dictionary for easy lookup
categories_dict = {cat['id']: cat for cat in data_array}

# STEP 1: Merge duplicates
print("\n=== MERGING DUPLICATES ===")

# Merge computer-repair into computerlaptoprepairs
if 'computer-repair' in categories_dict and 'computerlaptoprepairs' in categories_dict:
    categories_dict['computerlaptoprepairs']['providers'].extend(
        categories_dict['computer-repair']['providers']
    )
    del categories_dict['computer-repair']
    print("✓ Merged computer-repair -> computerlaptoprepairs")

# Merge medical into medicalstore
if 'medical' in categories_dict and 'medicalstore' in categories_dict:
    categories_dict['medicalstore']['providers'].extend(
        categories_dict['medical']['providers']
    )
    del categories_dict['medical']
    print("✓ Merged medical -> medicalstore")

# Merge insurance-agents into insuranceagent
if 'insurance-agents' in categories_dict and 'insuranceagent' in categories_dict:
    categories_dict['insuranceagent']['providers'].extend(
        categories_dict['insurance-agents']['providers']
    )
    del categories_dict['insurance-agents']
    print("✓ Merged insurance-agents -> insuranceagent")

# Merge financial-advisors into financialadvisor
if 'financial-advisors' in categories_dict and 'financialadvisor' in categories_dict:
    categories_dict['financialadvisor']['providers'].extend(
        categories_dict['financial-advisors']['providers']
    )
    del categories_dict['financial-advisors']
    print("✓ Merged financial-advisors -> financialadvisor")

# Merge nutritionists-dieticians (keep as dietician)
if 'nutritionists-dieticians' in categories_dict:
    # Rename to dietician
    cat = categories_dict['nutritionists-dieticians']
    cat['id'] = 'dietician'
    cat['name'] = 'Dietician'
    categories_dict['dietician'] = cat
    del categories_dict['nutritionists-dieticians']
    print("✓ Renamed nutritionists-dieticians -> dietician")

# STEP 2: Remove bike-scooter-repair
if 'bike-scooter-repair' in categories_dict:
    del categories_dict['bike-scooter-repair']
    print("✓ Removed bike-scooter-repair")

# STEP 3: Add new categories
print("\n=== ADDING NEW CATEGORIES ===")

new_categories = [
    {"id": "tiffin-service", "name": "Tiffin service", "icon": "🍱", "gu_name": "ટિફિન સર્વિસ"},
    {"id": "painter", "name": "Painter", "icon": "🎨", "gu_name": "પેઇન્ટર"},
    {"id": "ca", "name": "CA", "icon": "📊", "gu_name": "CA"},
    {"id": "tyre-dealer", "name": "Tyre Dealer", "icon": "🛞", "gu_name": "ટાયર ડીલર"},
    {"id": "battery-dealer", "name": "Battery Dealer", "icon": "🔋", "gu_name": "બેટરી ડીલર"},
    {"id": "govt-liasioning-agent", "name": "Govt Liasioning Agent", "icon": "🏛️", "gu_name": "સરકારી સંપર્ક એજન્ટ"},
    {"id": "ticket-booking-agent", "name": "Ticket booking agent", "icon": "🎫", "gu_name": "ટિકિટ બુકિંગ એજન્ટ"},
    {"id": "dance-teacher", "name": "Dance Teacher", "icon": "💃", "gu_name": "ડાન્સ ટીચર"},
    {"id": "music-teacher", "name": "Music Teacher", "icon": "🎵", "gu_name": "સંગીત શિક્ષક"},
    {"id": "2-wheeler-garage", "name": "2 wheeler garage", "icon": "🛵", "gu_name": "બાઈક ગેરેજ"},
    {"id": "4-wheeler-garage", "name": "4 wheeler garage", "icon": "🚗", "gu_name": "કાર ગેરેજ"},
    {"id": "house-cleaning-services", "name": "House Cleaning Services", "icon": "🧹", "gu_name": "ઘર સફાઈ સેવાઓ"},
    {"id": "packing-services", "name": "Packing Services", "icon": "📦", "gu_name": "પેકિંગ સેવાઓ"},
    {"id": "influencer", "name": "Influencer", "icon": "📱", "gu_name": "ઇન્ફ્લુએન્સર"},
    {"id": "software-developer", "name": "Software Developer / App Developer", "icon": "💻", "gu_name": "સોફ્ટવેર ડેવલપર"},
    {"id": "musician", "name": "Musician", "icon": "🎸", "gu_name": "સંગીતકાર"},
    {"id": "teachers", "name": "Teachers", "icon": "👨‍🏫", "gu_name": "શિક્ષકો"},
    {"id": "mochi-shoe-maker", "name": "Mochi / Shoe Maker", "icon": "👞", "gu_name": "મોચી"},
    {"id": "house-maid", "name": "House Maid / Home Support Assistants", "icon": "🧹", "gu_name": "ઘરકામ સહાયક"},
    {"id": "cook", "name": "Cook", "icon": "👨‍🍳", "gu_name": "રસોઇયા"},
    {"id": "internet-broadband", "name": "Internet Broadband Service Provider", "icon": "🌐", "gu_name": "ઇન્ટરનેટ બ્રોડબેન્ડ"},
    {"id": "tailor", "name": "Tailor", "icon": "🧵", "gu_name": "દરજી"},
]

added_count = 0
for new_cat in new_categories:
    if new_cat['id'] not in categories_dict:
        categories_dict[new_cat['id']] = {
            **new_cat,
            "providers": []
        }
        added_count += 1
        print(f"✓ Added: {new_cat['name']}")

print(f"\n✓ Added {added_count} new categories")

# Convert back to array
final_data = list(categories_dict.values())

# Sort by name for better organization
final_data.sort(key=lambda x: x['name'])

print(f"\n=== FINAL STATS ===")
print(f"Total categories: {len(final_data)}")

# Write back to file
output_content = f"""// Bhuj Online - Static Data Layer
// ----------------------------------------------------
// NOTE: Data is now embedded directly as JSON to avoid CSV parsing issues.
// ----------------------------------------------------

// Embedded Data (Converted from CSV)
window.bhujData = {json.dumps(final_data, ensure_ascii=False, indent=4)};

// Helper Functions
// ----------------------------------------------------

window.initializeData = async function () {{
    // No-op: Data is already loaded synchronously.
    console.log("Data loaded from static JSON.");
}};

window.getAllCategories = function () {{
    return window.bhujData.map(c => ({{
        id: c.id,
        name: c.name,
        icon: c.icon,
        gu_name: c.gu_name
    }}));
}};

window.getProviders = function (catId) {{
    return window.bhujData.find(c => c.id === catId) || null;
}};
"""

with open("assets/js/data.js", "w", encoding="utf-8") as f:
    f.write(output_content)

print(f"\n✅ SUCCESS! Restructuring complete.")
print(f"✓ Backup saved to: {backup_file}")
print(f"✓ New data.js written with {len(final_data)} categories")
