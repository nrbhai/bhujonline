import csv
import json
from collections import defaultdict

# Read CSV file
csv_file = 'data.csv'
js_file = 'assets/js/data.js'

# Parse CSV and organize by category
categories_data = defaultdict(lambda: {'providers': [], 'seen': set()})

# Try different encodings
encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
data_rows = []

for encoding in encodings:
    try:
        with open(csv_file, 'r', encoding=encoding) as f:
            reader = csv.DictReader(f)
            data_rows = list(reader)
        print(f"✅ Successfully read CSV with {encoding} encoding")
        break
    except UnicodeDecodeError:
        continue
else:
    print("❌ Could not read CSV with any encoding")
    exit(1)

for row in data_rows:
        category = row['Category'].strip()
        name = row['Name'].strip()
        phone = row['Phone'].strip()
        area = row['Area'].strip()
        tags = row['Tags'].strip() if row['Tags'] else ''
        
        # Create unique key for deduplication (category + name + phone)
        unique_key = f"{category}|{name}|{phone}"
        
        # Skip if duplicate
        if unique_key in categories_data[category]['seen']:
            print(f"Skipping duplicate: {name} in {category}")
            continue
        
        categories_data[category]['seen'].add(unique_key)
        
        # Parse tags
        tags_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
        
        # Create provider object
        provider = {
            'name': name,
            'phone': phone,
            'area': area,
            'tags': tags_list,
            'webpage': ''  # Empty webpage field
        }
        
        categories_data[category]['providers'].append(provider)

# Create categories list
categories = []
for category_name in sorted(categories_data.keys()):
    if not categories_data[category_name]['providers']:
        continue
    
    # Create category ID (lowercase, spaces to dashes)
    category_id = category_name.lower().replace(' ', '-')
    
    # Determine icon based on category name - Comprehensive mapping
    icon_map = {
        # Services
        'electrician': '⚡',
        'plumber': '🔧',
        'carpenter': '🪚',
        'painter': '🎨',
        'ac service': '❄️',
        'ac/fridge repair': '❄️',
        'pest control': '🐛',
        'interior designer': '🏠',
        'mason': '🧱',
        'welder': '🔥',
        'mechanic': '🔧',
        'cleaning service': '🧹',
        
        # Health & Medical
        'medical': '🏥',
        'doctor': '👨‍⚕️',
        'hospital': '🏥',
        'hospitals': '🏥',
        'clinic': '🏥',
        'pharmacy': '💊',
        'opticians': '👓',
        'dental': '🦷',
        'physiotherapy': '💪',
        
        # Transportation
        'taxi': '🚕',
        'auto': '🛺',
        '2 wheeler garage': '🏍️',
        '4 wheeler garage': '🚗',
        'car rental': '🚗',
        'tours & travels': '✈️',
        'transport': '🚛',
        
        # Legal & Professional
        'lawyer': '⚖️',
        'ca': '💼',
        'chartered accountant': '💼',
        'financial advisor': '💰',
        'insurance': '🛡️',
        'real estate': '🏢',
        'estate agent': '🏢',
        
        # Technology
        'computer': '💻',
        'mobile': '📱',
        'laptop repair': '💻',
        'cctv': '📹',
        'software': '💿',
        'website designer': '🌐',
        'web development': '🌐',
        
        # Beauty & Wellness
        'salon': '💇',
        'spa': '💆',
        'gym': '💪',
        'fitness': '💪',
        'yoga': '🧘',
        'beauty parlour': '💄',
        
        # Food & Hospitality
        'restaurant': '🍽️',
        'hotel': '🏨',
        'cafe': '☕',
        'bakery': '🍰',
        'caterer': '🍱',
        'sweet shop': '🍬',
        'catering': '🍱',
        
        # Education
        'education': '📚',
        'tuition': '📖',
        'school': '🏫',
        'coaching': '📖',
        'training': '📖',
        'dance class': '💃',
        'music class': '🎵',
        
        # Retail & Shopping
        'jeweller': '💎',
        'clothing': '👔',
        'electronics': '📺',
        'mobile shop': '📱',
        'stationery': '✏️',
        'bookstore': '📚',
        'grocery': '🛒',
        'supermarket': '🛒',
        'general store': '🛒',
        
        # Professional Services
        'photographer': '📸',
        'printing': '🖨️',
        'xerox': '📄',
        'courier': '📦',
        'event planner': '🎉',
        'security': '🛡️',
        'packers and movers': '📦',
        
        # Construction & Materials
        'hardware': '🔨',
        'building material': '🧱',
        'steel': '🏗️',
        'cement': '🏗️',
        'tiles': '🏗️',
        
        # Agriculture & Animals
        'veterinary': '🐾',
        'pet shop': '🐕',
        'agriculture': '🌾',
        'seeds': '🌱',
        
        # Specialized Services
        'astrologer': '🔮',
        'electricals': '💡',
        'solar panel': '☀️',
        'water purifier': '💧',
        'gujarati typist': '⌨️',
        'dastavej / document writers': '📝',
        'importers / exporters': '🌍',
        'chartered engineer': '👷',
        'architect': '📐',
    }
    
    icon = icon_map.get(category_name.lower(), '📋')
    
    category_obj = {
        'id': category_id,
        'name': category_name,
        'icon': icon,
        'gu_name': category_name,  # Can be updated with Gujarati names later
        'providers': categories_data[category_name]['providers']
    }
    
    categories.append(category_obj)

# Write to JavaScript file
with open(js_file, 'w', encoding='utf-8') as f:
    f.write('// Auto-generated from data.csv\n')
    f.write('// Do not edit manually - use data.csv and regenerate\n\n')
    f.write('const categoriesData = ')
    f.write(json.dumps(categories, indent=2, ensure_ascii=False))
    f.write(';\n\n')
    
    # Add helper functions
    f.write('''
// Helper function to get all categories
function getAllCategories() {
    return categoriesData;
}

// Helper function to get providers by category ID
function getProviders(categoryId) {
    const category = categoriesData.find(cat => cat.id === categoryId);
    return category || null;
}

// Export for use in script.js
if (typeof window !== 'undefined') {
    window.getAllCategories = getAllCategories;
    window.getProviders = getProviders;
}
''')

print(f"✅ Converted {len(categories)} categories")
total_providers = sum(len(cat['providers']) for cat in categories)
print(f"✅ Total providers: {total_providers}")
print(f"✅ Written to {js_file}")
