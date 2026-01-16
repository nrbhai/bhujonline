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
    
    # Complete icon mapping for all categories
    icon_map = {
        # Home Services
        'electrician': '⚡',
        'plumber': '🔧',
        'carpenter': '🪚',
        'painter': '🎨',
        'ac/fridge repair': '❄️',
        'ac service': '❄️',
        'pest control': '🐛',
        'interior designer': '🏠',
        'mason': '🧱',
        'masons': '🧱',
        'welder': '🔥',
        'cleaning service': '🧹',
        'laundry / dhobi': '👕',
        'tank cleaning': '💧',
        'pop/false ceiling': '🏠',
        'tiles fitter': '🏗️',
        'modular kitchen': '🍴',
        
        # Health & Medical
        'medical': '🏥',
        'doctor': '👨‍⚕️',
        'hospital': '🏥',
        'hospitals': '🏥',
        'clinic': '🏥',
        'pharmacy': '💊',
        'medical store': '💊',
        'opticians': '👓',
        'dental': '🦷',
        'physiotherapy': '💪',
        'physiotherapists': '💪',
        'blood bank': '🩸',
        'ambulance': '🚑',
        'laboratories': '🔬',
        'nurses': '👩‍⚕️',
        'nutritionists/dieticians': '🥗',
        'dietician': '🥗',
        
        # Transportation
        'taxi': '🚕',
        'auto': '🛺',
        'auto/taxi': '🚕',
        'bike/scooter repair': '🏍️',
        'car mechanic': '🚗',
        'tours & travels': '✈️',
        'transport/tempo services': '🚛',
        'packers & movers': '📦',
        'courier services': '📦',
        'tyre/puncture shop': '🚗',
        
        # Legal & Financial
        'lawyer': '⚖️',
        'legal services/ lawyer': '⚖️',
        'notary': '📜',
        'notary/legal services': '📜',
        'ca/tax consultants': '💼',
        'chartered accountant': '💼',
        'financial advisor': '💰',
        'insurance': '🛡️',
        'insurance agent': '🛡️',
        'insurance agents': '🛡️',
        'gst/accounting services': '💼',
        'accounting services': '💼',
        'share brokers': '📈',
        'stock market servicee': '📈',
        'mutual fund advisors': '💰',
        
        # Real Estate
        'real estate': '🏢',
        'real estate agents': '🏢',
        'estate agent': '🏢',
        'house/shop rentals': '🏘️',
        'pg/hostels': '🏠',
        'homestay': '🏡',
        'homestays': '🏡',
        
        # Technology & IT
        'computer': '💻',
        'computer repair': '💻',
        'computer laptop repairs': '💻',
        'mobile': '📱',
        'laptop repair': '💻',
        'cctv': '📹',
        'cctv installation': '📹',
        'software': '💿',
        'website designer': '🌐',
        'website designers': '🌐',
        'web development': '🌐',
        'digital marketing': '📱',
        'graphic designers': '🎨',
        
        # Beauty & Wellness
        'salon': '💇',
        'spa': '💆',
        'gym': '💪',
        'fitness': '💪',
        'yoga': '🧘',
        'yoga fitness trainers': '🧘',
        'yoga/fitness trainers': '🧘',
        'beauty parlour': '💄',
        
        # Food & Hospitality
        'restaurant': '🍽️',
        'restaurants': '🍽️',
        'hotel': '🏨',
        'hotels': '🏨',
        'cafe': '☕',
        'bakery': '🍰',
        'caterer': '🍱',
        'caterars': '🍱',
        'caterers': '🍱',
        'sweet shop / mithai': '🍬',
        'sweet shops/mithai': '🍬',
        'cold storage': '❄️',
        'ice delivery': '🧊',
        'milk delivery': '🥛',
        
        # Education & Training
        'education': '📚',
        'tuition': '📖',
        'tuition classes': '📖',
        'school': '🏫',
        'schools': '🏫',
        'coaching': '📖',
        'coaching classes': '📖',
        'training': '📖',
        'teachers': '👨‍🏫',
        'dance class': '💃',
        'music class': '🎵',
        
        # Retail & Shopping
        'jeweller': '💎',
        'jewellers': '💎',
        'clothing': '👔',
        'cloths merchant': '👔',
        'fashion designer': '👗',
        'electronics': '📺',
        'mobile shop': '📱',
        'stationery': '✏️',
        "stationer's": '✏️',
        'bookstore': '📚',
        'grocery': '🛒',
        'kirana stores': '🛒',
        'supermarket': '🛒',
        'general store': '🛒',
        'electrical stores': '💡',
        'hardware stores': '🔨',
        
        # Professional Services
        'photographer/videographer': '📸',
        'photographers / videographers': '📸',
        'printing & flex banner': '🖨️',
        'xerox': '📄',
        'event planner': '🎉',
        'event planners': '🎉',
        'decoration services': '🎈',
        'decorators': '🎈',
        'tent & sound system': '🎪',
        'flower shops': '💐',
        'tailor': '✂️',
        
        # Construction & Materials
        'hardware': '🔨',
        'construction material': '🏗️',
        'building material': '🧱',
        'steel': '🏗️',
        'cement': '🏗️',
        'tiles': '🏗️',
        'civil contractor': '👷',
        'aluminium fabrication': '🔩',
        
        # Agriculture & Animals
        'veterinary': '🐾',
        'vetenary services / pet services': '🐾',
        'veterinary/animal care': '🐾',
        'pet shop': '🐕',
        'agriculture': '🌾',
        'agricultural implements': '🚜',
        'seeds': '🌱',
        
        # Specialized Services
        'astrologer': '🔮',
        'astrologer / vaastu': '🔮',
        'astrology/vaastu': '🔮',
        'solar panel': '☀️',
        'solar panel installation': '☀️',
        'water purifier': '💧',
        'water purifier service': '💧',
        'ro water purifier': '💧',
        'water tanker services': '💧',
        'gujarati typist': '⌨️',
        'dastavej / document writers': '📝',
        'importers / exporters': '🌍',
        'chartered engineer': '👷',
        'architect': '📐',
        'inverter/battery dealers': '🔋',
        'banks': '🏦',
        'fire services': '🚒',
        'disaster repair': '🚨',
        'babysitters': '👶',
        'caretakers/elder care': '👴',
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
