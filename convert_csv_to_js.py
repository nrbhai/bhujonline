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
        print(f"✅ Successfully read CSV with {encoding} encoding")
        break
    except (UnicodeDecodeError, KeyError):
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
        webpage = row.get('Webpage', '').strip() if row.get('Webpage') else ''
        
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
            'webpage': webpage
        }
        
        categories_data[category]['providers'].append(provider)

# Create categories list
categories = []
for category_name in sorted(categories_data.keys()):
    if not categories_data[category_name]['providers']:
        continue
    
    # Create category ID (lowercase, spaces to dashes)
    category_id = category_name.lower().replace(' ', '-')
    
    # Complete icon mapping for all categories - Iconify (Multi-colored)
    icon_map = {
        # Home Services
        'electrician': 'noto-v1:high-voltage',
        'plumber': 'noto-v1:wrench',
        'carpenter': 'noto-v1:hammer',
        'painter': 'noto-v1:artist-palette',
        'ac/fridge repair': 'noto-v1:snowflake',
        'ac fridge repairer': 'noto-v1:snowflake',
        'ac service': 'noto-v1:snowflake',
        'pest control': 'noto-v1:bug',
        'interior designer': 'noto-v1:couch-and-lamp',
        'mason': 'noto-v1:brick',
        'masons': 'noto-v1:brick',
        'welder': 'noto-v1:fire',
        'cleaning service': 'noto-v1:broom',
        'laundry / dhobi': 'noto-v1:t-shirt',
        'tank cleaning': 'noto-v1:droplet',
        'pop/false ceiling': 'noto-v1:house',
        'tiles fitter': 'noto-v1:building-construction',
        'modular kitchen': 'noto-v1:fork-and-knife',
        
        # Health & Medical
        'medical': 'noto-v1:hospital',
        'doctor': 'noto-v1:health-worker',
        'allopathy doctors mbbs': 'noto-v1:health-worker',
        'allopathy doctors md ( specialist )': 'noto-v1:health-worker',
        'allopathy doctors md physician': 'noto-v1:health-worker',
        'ayurvedic doctors': 'noto-v1:health-worker',
        'homeopathy doctors': 'noto-v1:health-worker',
        'hospital': 'noto-v1:hospital',
        'hospitals': 'noto-v1:hospital',
        'clinic': 'noto-v1:hospital',
        'pharmacy': 'noto-v1:pill',
        'medical store': 'noto-v1:pill',
        'opticians': 'noto-v1:glasses',
        'dental': 'noto-v1:tooth',
        'physiotherapy': 'noto-v1:person-lifting-weights',
        'physiotherapists': 'noto-v1:person-lifting-weights',
        'blood bank': 'noto-v1:drop-of-blood',
        'ambulance': 'noto-v1:ambulance',
        'laboratories': 'noto-v1:test-tube',
        'nurses': 'noto-v1:health-worker',
        'nutritionists/dieticians': 'noto-v1:green-apple',
        'dietician': 'noto-v1:green-apple',
        
        # Transportation
        'taxi': 'noto-v1:taxi',
        'auto': 'noto-v1:auto-rickshaw',
        'auto/taxi': 'noto-v1:taxi',
        'bike/scooter repair': 'noto-v1:motorcycle',
        'car mechanic': 'noto-v1:automobile',
        'tours & travels': 'noto-v1:airplane',
        'transport/tempo services': 'noto-v1:delivery-truck',
        'packers & movers': 'noto-v1:package',
        'courier services': 'noto-v1:package',
        'tyre/puncture shop': 'noto-v1:automobile',
        
        # Legal & Financial
        'lawyer': 'noto-v1:balance-scale',
        'legal services/ lawyer': 'noto-v1:balance-scale',
        'notary': 'noto-v1:memo',
        'notary/legal services': 'noto-v1:memo',
        'ca': 'flat-color-icons:calculator',
        'ca ( chartered accountants )': 'flat-color-icons:calculator',
        'ca/tax consultants': 'flat-color-icons:calculator',
        'chartered accountant': 'flat-color-icons:calculator',
        'financial advisor': 'noto-v1:money-with-wings',
        'insurance': 'noto-v1:shield',
        'insurance agent': 'noto-v1:shield',
        'insurance agents': 'noto-v1:shield',
        'insurance companies': 'noto-v1:office-building',
        'gst/accounting services': 'flat-color-icons:document',
        'accounting services': 'flat-color-icons:document',
        'share brokers': 'noto-v1:chart-increasing',
        'stock market servicee': 'noto-v1:chart-increasing',
        'mutual fund advisors': 'noto-v1:money-bag',
        
        # Real Estate
        'real estate': 'noto-v1:office-building',
        'real estate agents': 'noto-v1:office-building',
        'estate agent': 'noto-v1:office-building',
        'house/shop rentals': 'noto-v1:house',
        'pg/hostels': 'noto-v1:bed',
        'homestay': 'noto-v1:house-with-garden',
        'homestays': 'noto-v1:house-with-garden',
        
        # Technology & IT
        'computer': 'noto-v1:laptop',
        'computer repair': 'noto-v1:laptop',
        'computer laptop repairs': 'noto-v1:laptop',
        'computer laptop sales': 'noto-v1:laptop',
        'mobile': 'noto-v1:mobile-phone',
        'laptop repair': 'noto-v1:laptop',
        'cctv': 'noto-v1:video-camera',
        'cctv installation': 'noto-v1:video-camera',
        'software': 'flat-color-icons:data-configuration',
        'website designer': 'flat-color-icons:web-design',
        'website designers': 'flat-color-icons:web-design',
        'web development': 'flat-color-icons:web-design',
        'digital marketing': 'noto-v1:megaphone',
        'graphic designers': 'noto-v1:artist-palette',
        
        # Beauty & Wellness
        'salon': 'noto-v1:scissors',
        'spa': 'noto-v1:person-getting-massage',
        'gym': 'noto-v1:person-lifting-weights',
        'fitness': 'noto-v1:person-lifting-weights',
        'yoga': 'noto-v1:person-in-lotus-position',
        'yoga fitness trainers': 'noto-v1:person-in-lotus-position',
        'yoga/fitness trainers': 'noto-v1:person-in-lotus-position',
        'beauty parlour': 'noto-v1:lipstick',
        'hair stylist ( m / f )': 'noto-v1:scissors',
        
        # Food & Hospitality
        'restaurant': 'noto-v1:fork-and-knife-with-plate',
        'restaurants': 'noto-v1:fork-and-knife-with-plate',
        'hotel': 'noto-v1:hotel',
        'hotels': 'noto-v1:hotel',
        'cafe': 'noto-v1:hot-beverage',
        'bakery': 'noto-v1:birthday-cake',
        'caterer': 'noto-v1:pot-of-food',
        'caterars': 'noto-v1:pot-of-food',
        'caterers': 'noto-v1:pot-of-food',
        'sweet shop / mithai': 'noto-v1:candy',
        'sweet shops/mithai': 'noto-v1:candy',
        'cold storage': 'noto-v1:snowflake',
        'ice delivery': 'noto-v1:ice-cream',
        'milk delivery': 'noto-v1:glass-of-milk',
        
        # Education & Training
        'education': 'noto-v1:graduation-cap',
        'tuition': 'noto-v1:books',
        'tuition classes': 'noto-v1:books',
        'school': 'noto-v1:school',
        'schools': 'noto-v1:school',
        'coaching': 'noto-v1:books',
        'coaching classes': 'noto-v1:books',
        'training': 'noto-v1:books',
        'teachers': 'noto-v1:teacher',
        'dance class': 'noto-v1:musical-notes',
        'music class': 'noto-v1:musical-notes',
        
        # Retail & Shopping
        'jeweller': 'noto-v1:gem-stone',
        'jewellers': 'noto-v1:gem-stone',
        'clothing': 'noto-v1:t-shirt',
        'cloths merchant': 'noto-v1:t-shirt',
        'fashion designer': 'noto-v1:scissors',
        'electronics': 'noto-v1:television',
        'mobile shop': 'noto-v1:mobile-phone',
        'stationery': 'noto-v1:pencil',
        "stationer's": 'noto-v1:pencil',
        'bookstore': 'noto-v1:books',
        'grocery': 'noto-v1:shopping-cart',
        'kirana stores': 'noto-v1:shopping-cart',
        'supermarket': 'noto-v1:shopping-cart',
        'general store': 'noto-v1:shopping-cart',
        'electrical stores': 'noto-v1:light-bulb',
        'hardware stores': 'noto-v1:hammer-and-wrench',
        
        # Professional Services
        'photographer/videographer': 'noto-v1:camera',
        'photographers / videographers': 'noto-v1:camera',
        'printing & flex banner': 'noto-v1:printer',
        'xerox': 'noto-v1:printer',
        'event planner': 'noto-v1:calendar',
        'event planners': 'noto-v1:calendar',
        'decoration services': 'noto-v1:wrapped-gift',
        'decorators': 'noto-v1:wrapped-gift',
        'tent & sound system': 'noto-v1:speaker-high-volume',
        'flower shops': 'noto-v1:bouquet',
        'tailor': 'noto-v1:scissors',
        
        # Construction & Materials
        'hardware': 'noto-v1:hammer-and-wrench',
        'construction material': 'noto-v1:brick',
        'building material': 'noto-v1:brick',
        'steel': 'noto-v1:factory',
        'cement': 'noto-v1:brick',
        'tiles': 'noto-v1:building-construction',
        'civil contractor': 'noto-v1:construction-worker',
        'aluminium fabrication': 'noto-v1:factory',
        
        # Agriculture & Animals
        'veterinary': 'noto-v1:paw-prints',
        'veterinary doctor': 'noto-v1:health-worker',
        'vetenary services / pet services': 'noto-v1:paw-prints',
        'pet products': 'noto-v1:paw-prints',
        'veterinary/animal care': 'noto-v1:health-worker',
        'pet shop': 'noto-v1:dog',
        'agriculture': 'noto-v1:sheaf-of-rice',
        'agricultural implements': 'noto-v1:tractor',
        'agricultural equipments': 'noto-v1:tractor',
        'seeds': 'noto-v1:seedling',
        
        # Specialized Services
        'astrologer': 'noto-v1:star',
        'astrologer / vaastu': 'noto-v1:star',
        'astrology/vaastu': 'noto-v1:star',
        'solar panel': 'noto-v1:sun',
        'solar panel installation': 'noto-v1:sun',
        'water purifier': 'noto-v1:droplet',
        'water purifier service': 'noto-v1:droplet',
        'ro water purifier': 'noto-v1:droplet',
        'water tanker services': 'noto-v1:delivery-truck',
        'gujarati typist': 'noto-v1:keyboard',
        'dastavej / document writers': 'noto-v1:memo',
        'importers / exporters': 'noto-v1:globe-showing-asia-australia',
        'chartered engineer': 'noto-v1:construction-worker',
        'architect': 'noto-v1:triangular-ruler',
        'inverter/battery dealers': 'noto-v1:battery',
        'banks': 'noto-v1:bank',
        'fire services': 'noto-v1:fire-engine',
        'disaster repair': 'noto-v1:fire-engine',
        'babysitters': 'noto-v1:baby',
        'caretakers/elder care': 'noto-v1:health-worker',
    }
    
    icon = icon_map.get(category_name.lower(), 'noto-v1:clipboard')
    
    # Gujarati name mapping
    gujarati_map = {
        # Home Services
        'electrician': 'ઇલેક્ટ્રીશિયન',
        'plumber': 'પ્લમ્બર',
        'carpenter': 'સુથાર',
        'painter': 'પેઇન્ટર',
        'ac/fridge repair': 'એસી/ફ્રિજ રિપેર',
        'ac fridge repairer': 'એસી/ફ્રિજ રિપેરર',
        'pest control': 'પેસ્ટ કંટ્રોલ',
        'interior designer': 'ઇન્ટીરિયર ડિઝાઇનર',
        'mason': 'રાજ',
        'masons': 'રાજ',
        'cleaning service': 'સફાઈ સેવા',
        'laundry / dhobi': 'ધોબી',
        'tank cleaning': 'ટાંકી સફાઈ',
        'pop/false ceiling': 'ફોલ્સ સીલિંગ',
        'tiles fitter': 'ટાઇલ્સ ફિટર',
        'modular kitchen': 'મોડ્યુલર કિચન',
        
        # Health & Medical
        'medical': 'મેડિકલ',
        'hospitals': 'હોસ્પિટલ',
        'medical store': 'દવાની દુકાન',
        'opticians': 'ચશ્મા',
        'blood bank': 'બ્લડ બેંક',
        'ambulance': 'એમ્બ્યુલન્સ',
        'laboratories': 'લેબોરેટરી',
        'nurses': 'નર્સ',
        'nutritionists/dieticians': 'પોષણ નિષ્ણાત',
        'dietician': 'આહાર નિષ્ણાત',
        'physiotherapists': 'ફિઝિયોથેરાપિસ્ટ',
        
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
        'ca/tax consultants': 'સીએ/ટેક્સ સલાહકાર',
        'financial advisor': 'નાણાકીય સલાહકાર',
        'insurance agent': 'વીમા એજન્ટ',
        'insurance agents': 'વીમા એજન્ટ',
        'gst/accounting services': 'જીએસટી/એકાઉન્ટિંગ',
        'accounting services': 'એકાઉન્ટિંગ સેવા',
        'share brokers': 'શેર બ્રોકર',
        'stock market servicee': 'સ્ટોક માર્કેટ સેવા',
        'mutual fund advisors': 'મ્યુચ્યુઅલ ફંડ સલાહકાર',
        
        # Real Estate
        'real estate agents': 'રીઅલ એસ્ટેટ એજન્ટ',
        'estate agent': 'એસ્ટેટ એજન્ટ',
        'house/shop rentals': 'ઘર/દુકાન ભાડે',
        'pg/hostels': 'પીજી/હોસ્ટેલ',
        'homestay': 'હોમસ્ટે',
        'homestays': 'હોમસ્ટે',
        
        # Technology
        'computer repair': 'કમ્પ્યુટર રિપેર',
        'computer laptop sales': 'કમ્પ્યુટર લેપટોપ વેચાણ',
        'cctv installation': 'સીસીટીવી ઇન્સ્ટોલેશન',
        'website designers': 'વેબસાઇટ ડિઝાઇનર',
        'digital marketing': 'ડિજિટલ માર્કેટિંગ',
        'graphic designers': 'ગ્રાફિક ડિઝાઇનર',
        
        # Beauty & Wellness
        'yoga/fitness trainers': 'યોગ/ફિટનેસ ટ્રેનર',
        'yoga fitness trainers': 'યોગ/ફિટનેસ ટ્રેનર',
        
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
        'jewellers': 'સોની',
        'cloths merchant': 'કપડાની દુકાન',
        'fashion designer': 'ફેશન ડિઝાઇનર',
        'kirana stores': 'કિરાણાની દુકાન',
        'electrical stores': 'ઇલેક્ટ્રિકલ સ્ટોર',
        'hardware stores': 'હાર્ડવેર સ્ટોર',
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
        
        # Animals & Agriculture
        'vetenary services / pet services': 'વેટરનરી સેવા',
        'veterinary/animal care': 'પશુ ચિકિત્સા',
        'agricultural implements': 'ખેતી સાધનો',
        
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
    
    gujarati_name = gujarati_map.get(category_name.lower(), category_name)
    
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

print(f"✅ Converted {len(categories)} categories")
total_providers = sum(len(cat['providers']) for cat in categories)
print(f"✅ Total providers: {total_providers}")
print(f"✅ Written to {js_file}")
