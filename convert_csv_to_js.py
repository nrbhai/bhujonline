import csv
import json
from collections import defaultdict

# Read CSV file
csv_file = 'data.csv'
js_file = 'assets/js/data.js'

# Parse CSV and organize by category
categories_data = defaultdict(lambda: {'providers': [], 'seen': set()})

# Try different encodings (utf-8-sig handles BOM)
encodings = ['utf-8-sig', 'utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
data_rows = []

for encoding in encodings:
    try:
        with open(csv_file, 'r', encoding=encoding) as f:
            reader = csv.DictReader(f)
            data_rows = list(reader)
        print(f"[OK] Successfully read CSV with {encoding} encoding")
        break
    except (UnicodeDecodeError, KeyError):
        continue
else:
    print("[ERROR] Could not read CSV with any encoding")
    exit(1)

for row in data_rows:
        category = row['Category'].strip()
        
        # Rename categories (English) - Add your renames here
        rename_map = {
            'Masons': 'Mason',
            'Ac fridge repairer': 'AC & Fridge Repair',
            'Allopathy Doctors MBBS': 'Doctors MBBS',
            'Allopathy Doctors MD ( Specialist )': 'Doctors MD ( Specialist )',
            'Allopathy Doctors MD Physician': 'Doctors MD Physician',
            # 'Old Name': 'New Name',
        }
        category = rename_map.get(category, category)
        
        name = row['Name'].strip()
        phone = row['Phone'].strip()
        area = row['Area'].strip()
        area = row['Area'].strip()
        tags = row['Tags'].strip() if row['Tags'] else ''
        webpage = row.get('Webpage', '').strip() if row.get('Webpage') else ''
        badge = row.get('Badge', '').strip() if row.get('Badge') else ''
        verified = row.get('Verified', '').strip() if row.get('Verified') else ''
        top_rated = row.get('Top Rated', '').strip() if row.get('Top Rated') else ''
        
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
            'webpage': webpage,
            'badge': badge,
            'verified': verified,
            'top_rated': top_rated
        }
        
        categories_data[category]['providers'].append(provider)

# Create categories list
categories = []
for category_name in sorted(categories_data.keys()):
    if not categories_data[category_name]['providers']:
        continue
    
    # Create category ID (lowercase, spaces to dashes)
    category_id = category_name.lower().replace(' ', '-')
    
    # Complete icon mapping for all categories - Native Emojis (3D Style)
    icon_map = {
        # Home Services
        'electrician': '⚡',
        'plumber': '🔧',
        'carpenter': '🔨',
        'painter': '🎨',
        'ac/fridge repair': '❄️',
        'ac fridge repairer': '❄️',
        'ac & fridge repair': '❄️',
        'ac service': '❄️',
        'pest control': '🪲',
        'interior designer': '🛋️',
        'mason': '🧱',
        'masons': '🧱',
        'welder': '🔥',
        'cleaning service': '🧹',
        'laundry / dhobi': '🧺',
        'tank cleaning': '💧',
        'pop/false ceiling': '🏠',
        'tiles fitter': '🏗️',
        'modular kitchen': '🍽️',
        
        # Health & Medical
        'medical': '🏥',
        'doctor': '👨‍⚕️',
        'doctors mbbs': '🩺',
        'doctors md ( specialist )': '⚕️',
        'doctors md physician': '💉',
        'ayurvedic doctors': '🌿',
        'homeopathy doctors': '💊',
        'hospital': '🏥',
        'hospitals': '🏥',
        'clinic': '🏥',
        'pharmacy': '💊', 
        'medical store': '💊',
        'opticians': '👓',
        'dental': '🦷',
        'physiotherapy': '🏋️',
        'physiotherapists': '🏋️',
        'blood bank': '🩸',
        'ambulance': '🚑',
        'laboratories': '🧪',
        'nurses': '👩‍⚕️',
        'nutritionists/dieticians': '🥗',
        'dietician': '🥗',
        
        # Transportation
        'taxi': '🚖',
        'auto': '🛺',
        'auto/taxi': '🚖',
        'bike/scooter repair': '🛵',
        'car mechanic': '🚘',
        'tours & travels': '✈️',
        'transport/tempo services': '🚚',
        'packers & movers': '📦',
        'courier services': '📦',
        'tyre/puncture shop': '🚙',
        
        # Legal & Financial
        'lawyer': '⚖️',
        'legal services/ lawyer': '⚖️',
        'notary': '📝',
        'notary/legal services': '📝',
        'ca': '🧮',
        'ca ( chartered accountants )': '🧮',
        'ca/tax consultants': '🧮',
        'chartered accountant': '🧮',
        'financial advisor': '📉',
        'insurance': '🛡️',
        'insurance agent': '🛡️',
        'insurance agents': '🛡️',
        'insurance companies': '🏢',
        'gst/accounting services': '📋',
        'accounting services': '📋',
        'share brokers': '💹',
        'stock market servicee': '💹',
        'mutual fund advisors': '💰',
        
        # Real Estate
        'real estate': '🏢',
        'real estate agents': '🏢',
        'estate agent': '🏘️',
        'house/shop rentals': '🏠',
        'pg/hostels': '🛏️',
        'homestay': '🏡',
        'homestays': '🏡',
        
        # Technology & IT
        'computer': '💻',
        'computer repair': '💻',
        'computer laptop repairs': '💻',
        'computer laptop sales': '💻',
        'mobile': '📱',
        'laptop repair': '💻',
        'cctv': '📹',
        'cctv installation': '📹',
        'software': '💾',
        'website designer': '🌐',
        'website designers': '🌐',
        'web development': '👨‍💻',
        'digital marketing': '📢',
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
        'hair stylist ( m / f )': '✂️',
        
        # Food & Hospitality
        'restaurant': '🍽️',
        'restaurants': '🍽️',
        'hotel': '🏨',
        'hotels': '🏨',
        'cafe': '☕',
        'bakery': '🎂',
        'caterer': '🥘',
        'caterars': '🥘',
        'caterers': '🥘',
        'sweet shop / mithai': '🍬',
        'sweet shops/mithai': '🍬',
        'cold storage': '❄️',
        'ice delivery': '🍦',
        'milk delivery': '🥛',
        
        # Education & Training
        'education': '🎓',
        'tuition': '📚',
        'tuition classes': '📚',
        'school': '🏫',
        'schools': '🏫',
        'coaching': '📖',
        'coaching classes': '📖',
        'training': '📝',
        'teachers': '👨‍🏫',
        'dance class': '💃',
        'music class': '🎵',
        
        # Retail & Shopping
        'jeweller': '💎',
        'jewellers': '💎',
        'clothing': '👕',
        'cloths merchant': '👕',
        'fashion designer': '👗',
        'electronics': '📺',
        'mobile shop': '📱',
        'stationery': '✏️',
        "stationer's": '✏️',
        'bookstore': '📚',
        'grocery': '🛒',
        'kirana stores': '🛒',
        'supermarket': '🛒',
        'general store': '🏪',
        'electrical stores': '💡',
        'hardware stores': '🛠️',
        
        # Professional Services
        'photographer/videographer': '📷',
        'photographers / videographers': '📷',
        'printing & flex banner': '🖨️',
        'xerox': '🖨️',
        'event planner': '📅',
        'event planners': '📅',
        'decoration services': '🎁',
        'decorators': '🎁',
        'tent & sound system': '🔊',
        'flower shops': '💐',
        'tailor': '🧵',
        
        # Construction & Materials
        'hardware': '🔨',
        'construction material': '🧱',
        'building material': '🧱',
        'steel': '🏗️',
        'cement': '🧱',
        'tiles': '⬛',
        'civil contractor': '👷',
        'aluminium fabrication': '⚙️',
        
        # Agriculture & Animals
        'veterinary': '🐾',
        'veterinary doctor': '👨‍⚕️',
        'vetenary services / pet services': '🐾',
        'pet products': '🦴',
        'veterinary/animal care': '🐕',
        'pet shop': '🐕',
        'agriculture': '🌾',
        'agricultural implements': '🚜',
        'agricultural equipments': '🚜',
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
        'water tanker services': '🚛',
        'gujarati typist': '⌨️',
        'dastavej / document writers': '✍️',
        'importers / exporters': '🌏',
        'chartered engineer': '👷',
        'architect': '📐',
        'inverter/battery dealers': '🔋',
        'banks': '🏦',
        'fire services': '🚒',
        'disaster repair': '🆘',
        'babysitters': '👶',
        'caretakers/elder care': '👴',
    }
    
    icon = icon_map.get(category_name.lower(), '📋')
    
    # Gujarati name mapping
    gujarati_map = {
        # Home Services
        'electrician': 'ઇલેક્ટ્રીશિયન',
        'plumber': 'પ્લમ્બર',
        'carpenter': 'સુથાર',
        'painter': 'રંગ કામ કરનાર',
        'ac/fridge repair': 'એસી/ફ્રિજ રિપેર',
        'ac fridge repairer': 'એસી/ફ્રિજ રિપેરર',
        'ac & fridge repair': 'એસી/ફ્રિજ રિપેર',
        'ac service': 'એસી સર્વિસ',
        'pest control': 'પેસ્ટ કંટ્રોલ',
        'interior designer': 'ઇન્ટીરિયર ડિઝાઇનર',
        'mason': 'કડીઓ',
        'masons': 'કડીઓ',
        'cleaning service': 'સફાઈ સેવા',
        'laundry / dhobi': 'ધોબી',
        'tank cleaning': 'ટાંકી સફાઈ',
        'pop/false ceiling': 'pop સીલિંગ',
        'tiles fitter': 'ટાઇલ્સ ફિટર',
        'modular kitchen': 'મોડ્યુલર કિચન',
        
        # Health & Medical
        'medical': 'મેડિકલ',
        'doctor': 'ડોક્ટર',
        'dental': 'ડેન્ટિસ્ટ',
        'clinic': 'ક્લિનિક',
        'pharmacy': 'ફાર્મસી',
        'doctors mbbs': 'MBBS ડોક્ટર',
        'doctors md ( specialist )': 'MD સ્પેશિયાલિસ્ટ ડોક્ટર',
        'doctors md physician': 'MD ફિઝિશિયન',
        'hospitals': 'હોસ્પિટલ',
        'medical store': 'દવાની દુકાન',
        'opticians': 'ચશ્મા બનાવનાર',
        'blood bank': 'બ્લડ બેંક',
        'ambulance': 'એમ્બ્યુલન્સ',
        'laboratories': 'લેબોરેટરી',
        'nurses': 'નર્સ',
        'nutritionists/dieticians': 'પોષણ નિષ્ણાત',
        'dietician': 'આહાર નિષ્ણાત',
        'physiotherapists': 'ફિઝિયોથેરાપિસ્ટ',
        'ayurvedic doctors': 'આયુર્વેદિક ડોક્ટર',
        'homeopathy doctors': 'હોમિયોપેથી ડોક્ટર',
        
        # Transportation
        'auto/taxi': 'ઓટો/ટેક્સી',
        'bike/scooter repair': 'બાઇક/સ્કૂટર રિપેર',
        'car mechanic': 'કાર મિકેનિક',
        'tours & travels': 'ટુર્સ અને ટ્રાવેલ્સ',
        'transport/tempo services': 'ટ્રાન્સપોર્ટ સેવા',
        'packers & movers': 'પેકર્સ અને મૂવર્સ',
        'courier services': 'કુરિયર સેવા',
        'tyre/puncture shop': 'ટાયર/પંચર',
        
        # Legal & Financial
        'legal services/ lawyer': 'વકીલ',
        'notary': 'નોટરી',
        'notary/legal services': 'નોટરી સેવા',
        'notary/legal services': 'નોટરી સેવા',
        'ca': 'CA',
        'chartered accountant': 'ચાર્ટર્ડ એકાઉન્ટન્ટ',
        'ca ( chartered accountants )': 'CA (ચાર્ટર્ડ એકાઉન્ટન્ટ)',
        'ca/tax consultants': 'સીએ/ટેક્સ સલાહકાર',
        'financial advisor': 'નાણાકીય સલાહકાર',
        'insurance agent': 'વીમા એજન્ટ',
        'insurance agents': 'વીમા એજન્ટ',
        'gst/accounting services': 'જીએસટી/એકાઉન્ટિંગ',
        'accounting services': 'એકાઉન્ટિંગ સેવા',
        'share brokers': 'શેર બ્રોકર',
        'stock market servicee': 'સ્ટોક માર્કેટ સેવા',
        'mutual fund advisors': 'મ્યુચ્યુઅલ ફંડ સલાહકાર',
        'insurance companies': 'વીમા કંપનીઓ',
        
        # Real Estate
        'real estate agents': 'રીઅલ એસ્ટેટ દલાલ',
        'estate agent': 'એસ્ટેટ એજન્ટ',
        'house/shop rentals': 'ઘર/દુકાન ભાડે આપનાર',
        'pg/hostels': 'પીજી/હોસ્ટેલ',
        'homestay': 'હોમસ્ટે',
        'homestays': 'હોમસ્ટે',
        
        # Technology
        'computer': 'કમ્પ્યુટર',
        'mobile': 'મોબાઈલ',
        'laptop repair': 'લેપટોપ રિપેર',
        'cctv': 'સીસીટીવી',
        'software': 'સોફ્ટવેર',
        'computer repair': 'કમ્પ્યુટર રિપેર',
        'computer laptop sales': 'કમ્પ્યુટર લેપટોપ વેચાણ',
        'cctv installation': 'સીસીટીવી ઇન્સ્ટોલેશન',
        'website designers': 'વેબસાઇટ ડિઝાઇનર',
        'digital marketing': 'ડિજિટલ માર્કેટિંગ',
        'graphic designers': 'ગ્રાફિક ડિઝાઇનર',
        
        # Beauty & Wellness
        'gym': 'જિમ',
        'salon': 'સલૂન',
        'spa': 'સ્પા',
        'beauty parlour': 'બ્યુટી પાર્લર',
        'yoga/fitness trainers': 'યોગ/ફિટનેસ ટ્રેનર',
        'yoga fitness trainers': 'યોગ/ફિટનેસ ટ્રેનર',
        'hair stylist ( m / f )': 'હેર સ્ટાઈલિસ્ટ (સ્ત્રી/પુરુષ)',
        
        # Food & Hospitality
        'restaurants': 'રેસ્ટોરન્ટ',
        'hotels': 'હોટેલ',
        'caterars': 'કેટરિંગ',
        'caterers': 'કેટરિંગ',
        'sweet shop / mithai': 'મીઠાઈની દુકાન',
        'sweet shops/mithai': 'મીઠાઈની દુકાન',
        'cold storage': 'કોલ્ડ સ્ટોરેજ',
        'ice delivery': 'બરફ ડિલિવરી',
        'milk delivery': 'દૂધ ડિલિવરી',
        
        # Education
        'tuition classes': 'ટ્યુશન ક્લાસ',
        'schools': 'શાળા',
        'coaching classes': 'કોચિંગ ક્લાસ',
        'teachers': 'શિક્ષક',
        
        # Retail
        'jeweller': 'જ્વેલર્સ',
        'bookstore': 'પુસ્તક ભંડાર',
        'grocery': 'કરિયાણું',
        'supermarket': 'સુપરમાર્કેટ',
        'mobile shop': 'મોબાઈલ શોપ',
        'jewellers': 'સોની',
        'cloths merchant': 'કપડાની દુકાન',
        'fashion designer': 'ફેશન ડિઝાઇનર',
        'kirana stores': 'કિરાણાની દુકાન',
        'electrical stores': 'ઇલેક્ટ્રિકલ સ્ટોર',
        'hardware stores': 'હાર્ડવેર સ્ટોર',
        'hardware': 'હાર્ડવેર',
        "stationer's": 'સ્ટેશનરી',
        'stationery': 'સ્ટેશનરી',
        
        # Professional Services
        'photographer/videographer': 'ફોટોગ્રાફર',
        'photographers / videographers': 'ફોટોગ્રાફર',
        'printing & flex banner': 'પ્રિન્ટિંગ અને બેનર',
        'event planners': 'ઇવેન્ટ પ્લાનર',
        'decoration services': 'ડેકોરેશન સેવા',
        'decorators': 'ડેકોરેટર',
        'tent & sound system': 'ટેન્ટ અને સાઉન્ડ',
        'flower shops': 'ફૂલની દુકાન',
        'tailor': 'દરજી',
        
        # Construction
        'construction material': 'બાંધકામ સામગ્રી',
        'civil contractor': 'સિવિલ કોન્ટ્રાક્ટર',
        'aluminium fabrication': 'એલ્યુમિનિયમ ફેબ્રિકેશન',
        'steel': 'સ્ટીલ',
        'cement': 'સિમેન્ટ',
        'tiles': 'ટાઇલ્સ',
        
        # Animals & Agriculture
        'vetenary services / pet services': 'વેટરનરી સેવા',
        'veterinary/animal care': 'પશુ ચિકિત્સા',
        'veterinary doctor': 'વેટરનરી ડોક્ટર',
        'pet shop': 'પેટ શોપ',
        'pet products': 'પેટ પ્રોડક્ટ્સ',
        'agriculture': 'ખેતીવાડી',
        'seeds': 'બિયારણ',
        'agricultural implements': 'ખેતી સાધનો',
        'agricultural equipments': 'ખેતી સાધનો',
        
        # Specialized Services
        'astrologer / vaastu': 'જ્યોતિષી/વાસ્તુ',
        'astrology/vaastu': 'જ્યોતિષ/વાસ્તુ',
        'solar panel installation': 'સોલર પેનલ',
        'water purifier service': 'વોટર પ્યુરિફાયર',
        'ro water purifier': 'આરઓ વોટર પ્યુરિફાયર',
        'water tanker services': 'પાણીની ટાંકી સેવા',
        'gujarati typist': 'ગુજરાતી ટાઇપિસ્ટ',
        'dastavej / document writers': 'દસ્તાવેજ લેખક',
        'importers / exporters': 'આયાત/નિકાસ',
        'inverter/battery dealers': 'ઇન્વર્ટર/બેટરી',
        'banks': 'બેંક',
        'fire services': 'ફાયર સર્વિસ',
        'disaster repair': 'ડિઝાસ્ટર રિપેર',
        'babysitters': 'બેબીસીટર',
        'caretakers/elder care': 'કેરટેકર',
    }
    
    gujarati_name = gujarati_map.get(category_name.lower())
    if not gujarati_name:
        with open('missing.txt', 'a', encoding='utf-8') as log:
            log.write(category_name + '\n')
        gujarati_name = category_name
    
    category_obj = {
        'id': category_id,
        'name': category_name,
        'icon': icon,
        'gu_name': gujarati_name,
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

# Write to JSON file (for external use/updates)
json_file = 'data.json'
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(categories, f, indent=2, ensure_ascii=False)

print(f"[OK] Written to {json_file}")

print(f"[OK] Converted {len(categories)} categories")
total_providers = sum(len(cat['providers']) for cat in categories)
print(f"[OK] Total providers: {total_providers}")
print(f"[OK] Written to {js_file}")
