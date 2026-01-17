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
    
    # Complete icon mapping for all categories - Font Awesome
    icon_map = {
        # Home Services
        'electrician': 'fa-solid fa-bolt',
        'plumber': 'fa-solid fa-wrench',
        'carpenter': 'fa-solid fa-hammer',
        'painter': 'fa-solid fa-paint-roller',
        'ac/fridge repair': 'fa-solid fa-snowflake',
        'ac fridge repairer': 'fa-solid fa-snowflake',
        'ac service': 'fa-solid fa-snowflake',
        'pest control': 'fa-solid fa-bug',
        'interior designer': 'fa-solid fa-couch',
        'mason': 'fa-solid fa-trowel-bricks',
        'masons': 'fa-solid fa-trowel-bricks',
        'welder': 'fa-solid fa-fire',
        'cleaning service': 'fa-solid fa-broom',
        'laundry / dhobi': 'fa-solid fa-shirt',
        'tank cleaning': 'fa-solid fa-droplet',
        'pop/false ceiling': 'fa-solid fa-house',
        'tiles fitter': 'fa-solid fa-border-all',
        'modular kitchen': 'fa-solid fa-kitchen-set',
        
        # Health & Medical
        'medical': 'fa-solid fa-hospital',
        'doctor': 'fa-solid fa-user-doctor',
        'allopathy doctors mbbs': 'fa-solid fa-user-doctor',
        'allopathy doctors md ( specialist )': 'fa-solid fa-user-doctor',
        'allopathy doctors md physician': 'fa-solid fa-user-doctor',
        'ayurvedic doctors': 'fa-solid fa-user-doctor',
        'homeopathy doctors': 'fa-solid fa-user-doctor',
        'hospital': 'fa-solid fa-hospital',
        'hospitals': 'fa-solid fa-hospital',
        'clinic': 'fa-solid fa-hospital',
        'pharmacy': 'fa-solid fa-pills',
        'medical store': 'fa-solid fa-pills',
        'opticians': 'fa-solid fa-glasses',
        'dental': 'fa-solid fa-tooth',
        'physiotherapy': 'fa-solid fa-dumbbell',
        'physiotherapists': 'fa-solid fa-dumbbell',
        'blood bank': 'fa-solid fa-droplet',
        'ambulance': 'fa-solid fa-truck-medical',
        'laboratories': 'fa-solid fa-flask',
        'nurses': 'fa-solid fa-user-nurse',
        'nutritionists/dieticians': 'fa-solid fa-apple-whole',
        'dietician': 'fa-solid fa-apple-whole',
        
        # Transportation
        'taxi': 'fa-solid fa-taxi',
        'auto': 'fa-solid fa-taxi',
        'auto/taxi': 'fa-solid fa-taxi',
        'bike/scooter repair': 'fa-solid fa-motorcycle',
        'car mechanic': 'fa-solid fa-car',
        'tours & travels': 'fa-solid fa-plane',
        'transport/tempo services': 'fa-solid fa-truck',
        'packers & movers': 'fa-solid fa-box',
        'courier services': 'fa-solid fa-box',
        'tyre/puncture shop': 'fa-solid fa-car',
        
        # Legal & Financial
        'lawyer': 'fa-solid fa-scale-balanced',
        'legal services/ lawyer': 'fa-solid fa-scale-balanced',
        'notary': 'fa-solid fa-file-signature',
        'notary/legal services': 'fa-solid fa-file-signature',
        'ca': 'fa-solid fa-calculator',
        'ca ( chartered accountants )': 'fa-solid fa-calculator',
        'ca/tax consultants': 'fa-solid fa-calculator',
        'chartered accountant': 'fa-solid fa-calculator',
        'financial advisor': 'fa-solid fa-money-bill-trend-up',
        'insurance': 'fa-solid fa-shield-halved',
        'insurance agent': 'fa-solid fa-shield-halved',
        'insurance agents': 'fa-solid fa-shield-halved',
        'insurance companies': 'fa-solid fa-building',
        'gst/accounting services': 'fa-solid fa-file-invoice-dollar',
        'accounting services': 'fa-solid fa-file-invoice-dollar',
        'share brokers': 'fa-solid fa-chart-line',
        'stock market servicee': 'fa-solid fa-chart-line',
        'mutual fund advisors': 'fa-solid fa-money-bill-trend-up',
        
        # Real Estate
        'real estate': 'fa-solid fa-building',
        'real estate agents': 'fa-solid fa-building',
        'estate agent': 'fa-solid fa-building',
        'house/shop rentals': 'fa-solid fa-house',
        'pg/hostels': 'fa-solid fa-bed',
        'homestay': 'fa-solid fa-house-user',
        'homestays': 'fa-solid fa-house-user',
        
        # Technology & IT
        'computer': 'fa-solid fa-laptop',
        'computer repair': 'fa-solid fa-laptop',
        'computer laptop repairs': 'fa-solid fa-laptop',
        'computer laptop sales': 'fa-solid fa-laptop',
        'mobile': 'fa-solid fa-mobile-screen',
        'laptop repair': 'fa-solid fa-laptop',
        'cctv': 'fa-solid fa-video',
        'cctv installation': 'fa-solid fa-video',
        'software': 'fa-solid fa-code',
        'website designer': 'fa-solid fa-code',
        'website designers': 'fa-solid fa-code',
        'web development': 'fa-solid fa-code',
        'digital marketing': 'fa-solid fa-bullhorn',
        'graphic designers': 'fa-solid fa-palette',
        
        # Beauty & Wellness
        'salon': 'fa-solid fa-scissors',
        'spa': 'fa-solid fa-spa',
        'gym': 'fa-solid fa-dumbbell',
        'fitness': 'fa-solid fa-dumbbell',
        'yoga': 'fa-solid fa-person-praying',
        'yoga fitness trainers': 'fa-solid fa-person-praying',
        'yoga/fitness trainers': 'fa-solid fa-person-praying',
        'beauty parlour': 'fa-solid fa-scissors',
        'hair stylist ( m / f )': 'fa-solid fa-scissors',
        
        # Food & Hospitality
        'restaurant': 'fa-solid fa-utensils',
        'restaurants': 'fa-solid fa-utensils',
        'hotel': 'fa-solid fa-hotel',
        'hotels': 'fa-solid fa-hotel',
        'cafe': 'fa-solid fa-mug-hot',
        'bakery': 'fa-solid fa-cake-candles',
        'caterer': 'fa-solid fa-utensils',
        'caterars': 'fa-solid fa-utensils',
        'caterers': 'fa-solid fa-utensils',
        'sweet shop / mithai': 'fa-solid fa-candy-cane',
        'sweet shops/mithai': 'fa-solid fa-candy-cane',
        'cold storage': 'fa-solid fa-snowflake',
        'ice delivery': 'fa-solid fa-ice-cream',
        'milk delivery': 'fa-solid fa-bottle-droplet',
        
        # Education & Training
        'education': 'fa-solid fa-graduation-cap',
        'tuition': 'fa-solid fa-book',
        'tuition classes': 'fa-solid fa-book',
        'school': 'fa-solid fa-school',
        'schools': 'fa-solid fa-school',
        'coaching': 'fa-solid fa-book',
        'coaching classes': 'fa-solid fa-book',
        'training': 'fa-solid fa-book',
        'teachers': 'fa-solid fa-chalkboard-user',
        'dance class': 'fa-solid fa-music',
        'music class': 'fa-solid fa-music',
        
        # Retail & Shopping
        'jeweller': 'fa-solid fa-gem',
        'jewellers': 'fa-solid fa-gem',
        'clothing': 'fa-solid fa-shirt',
        'cloths merchant': 'fa-solid fa-shirt',
        'fashion designer': 'fa-solid fa-scissors',
        'electronics': 'fa-solid fa-tv',
        'mobile shop': 'fa-solid fa-mobile-screen',
        'stationery': 'fa-solid fa-pen',
        "stationer's": 'fa-solid fa-pen',
        'bookstore': 'fa-solid fa-book',
        'grocery': 'fa-solid fa-cart-shopping',
        'kirana stores': 'fa-solid fa-cart-shopping',
        'supermarket': 'fa-solid fa-cart-shopping',
        'general store': 'fa-solid fa-cart-shopping',
        'electrical stores': 'fa-solid fa-lightbulb',
        'hardware stores': 'fa-solid fa-screwdriver-wrench',
        
        # Professional Services
        'photographer/videographer': 'fa-solid fa-camera',
        'photographers / videographers': 'fa-solid fa-camera',
        'printing & flex banner': 'fa-solid fa-print',
        'xerox': 'fa-solid fa-print',
        'event planner': 'fa-solid fa-calendar-days',
        'event planners': 'fa-solid fa-calendar-days',
        'decoration services': 'fa-solid fa-gifts',
        'decorators': 'fa-solid fa-gifts',
        'tent & sound system': 'fa-solid fa-volume-high',
        'flower shops': 'fa-solid fa-seedling',
        'tailor': 'fa-solid fa-scissors',
        
        # Construction & Materials
        'hardware': 'fa-solid fa-screwdriver-wrench',
        'construction material': 'fa-solid fa-trowel-bricks',
        'building material': 'fa-solid fa-trowel-bricks',
        'steel': 'fa-solid fa-industry',
        'cement': 'fa-solid fa-trowel-bricks',
        'tiles': 'fa-solid fa-border-all',
        'civil contractor': 'fa-solid fa-helmet-safety',
        'aluminium fabrication': 'fa-solid fa-industry',
        
        # Agriculture & Animals
        'veterinary': 'fa-solid fa-paw',
        'veterinary doctor': 'fa-solid fa-user-doctor',
        'vetenary services / pet services': 'fa-solid fa-paw',
        'pet products': 'fa-solid fa-paw',
        'veterinary/animal care': 'fa-solid fa-user-doctor',
        'pet shop': 'fa-solid fa-dog',
        'agriculture': 'fa-solid fa-wheat-awn',
        'agricultural implements': 'fa-solid fa-tractor',
        'agricultural equipments': 'fa-solid fa-tractor',
        'seeds': 'fa-solid fa-seedling',
        
        # Specialized Services
        'astrologer': 'fa-solid fa-star',
        'astrologer / vaastu': 'fa-solid fa-star',
        'astrology/vaastu': 'fa-solid fa-star',
        'solar panel': 'fa-solid fa-solar-panel',
        'solar panel installation': 'fa-solid fa-solar-panel',
        'water purifier': 'fa-solid fa-droplet',
        'water purifier service': 'fa-solid fa-droplet',
        'ro water purifier': 'fa-solid fa-droplet',
        'water tanker services': 'fa-solid fa-truck-droplet',
        'gujarati typist': 'fa-solid fa-keyboard',
        'dastavej / document writers': 'fa-solid fa-file-pen',
        'importers / exporters': 'fa-solid fa-earth-americas',
        'chartered engineer': 'fa-solid fa-helmet-safety',
        'architect': 'fa-solid fa-compass-drafting',
        'inverter/battery dealers': 'fa-solid fa-car-battery',
        'banks': 'fa-solid fa-building-columns',
        'fire services': 'fa-solid fa-fire-extinguisher',
        'disaster repair': 'fa-solid fa-house-fire',
        'babysitters': 'fa-solid fa-baby',
        'caretakers/elder care': 'fa-solid fa-user-nurse',
    }
    
    icon = icon_map.get(category_name.lower(), 'fa-solid fa-list')
    
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
