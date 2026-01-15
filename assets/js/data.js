// Bhuj Online - Static Data Layer
// ----------------------------------------------------
// INSTRUCTIONS:
// 1. Paste your data inside the backticks `` below.
// 2. Format must be: Category, Name, Phone, Area, Tags (separated by |)
// 3. Do not remove the backticks.
// ----------------------------------------------------

const csvRaw = `
Category,Name,Phone,Area,Tags
Electrician,Mayur Electricians,9925185350,Station Road,Emergency
Electrician,Bhanu Electric Services,9879326177,Jubilee Ground,Maintenance
Electrician,Bapa Sitaram Electric,9979354091,Sanskar Nagar,Residential
Electrician,Ravi Electricals,9879177111,Old City,Commercial
Electrician,Sama Electrician,8128527027,Camp Area,24x7
Plumber,Krishna Plumbing Service,9925343091,Paddhar,Residential
Plumber,Girishbhai Plumber,9825708269,Din Dayal Nagar,10am-8pm
Plumber,Kaushik Patel Plumber,9909244093,Din Dayal Nagar,24x7
Plumber,Mehran Plumbing,9727456789,Bhuj HO,Highly Rated
Carpenter,Soylo Interior,9825227771,Bhuj HO,Furniture
Carpenter,Patel Home Services,9825166699,Madapar,Repairs
Carpenter,Tushar N Jamanapara,9426211234,Bhuj HO,Woodwork
Carpenter,L.R. Furniture,9825411222,Station Road,Decor
AC/Fridge Repair,Mannubhai AC Repair,7065012902,Bhuj HO,AC Repair
AC/Fridge Repair,Shital Cooling,09909418799,College Road,Cooling Specialist
AC/Fridge Repair,Gayatri Refrigeration,9825199888,Hospital Road,Fridge
Auto/Taxi,Raju Auto,9824211111,Bus Station,Auto
Auto/Taxi,Kutch Cabs,9909012312,Airport Road,Taxi
Medical,Jalaram Medico,02832250000,Hospital Road,24x7
Medical,Relief Pharmacy,02832222222,Bus Station,Chemist
Computer Repair,Pioneer Computer Services,9825034580,Station Road,Since 1993
CCTV Installation,Pioneer Computer Services,9825034580,Station Road,Since 1993
Masons,Sai Construction,9825211223,Bhuj HO,Contractor
Masons,Maheshbhai Mason,9727455666,Madapar,Brickwork
Masons,Total Secure Waterproofing,9879555444,Sanskar Nagar,Waterproofing
Masons,Handyservices In,9998877766,College Road,General Repairs
Kirana Stores,Swagat Grocery,9825111222,Station Road,Home Delivery
Kirana Stores,Dainik Needs,9909988777,Sanskar Nagar,Daily Essentials
Kirana Stores,Jalaram Provision,02832225566,Lal Tekri,Wholesale
Tuition Classes,Phoenix Education,9327164588,Uplipad Road,Commerce|Science
Tuition Classes,Sumati Study Centre,9825233444,Ghanshyam Nagar,5th to 12th
Tuition Classes,Seven Star Tuition,9925188888,Silver Park,English Medium
Schools,Army Public School,02832223309,Madhapar Road,CBSE
Schools,St Xaviers School,02832250011,Airport Road,English Medium
Schools,Mom's School,9825018335,New Lotus Colony,Kindergarten
Schools,Doon Public School,02832652001,Madhapar,Public School
Nurses,Shubh Aarogyam,9879512345,Bhuj HO,Home Care
Nurses,Care At Homes,9909911223,Sanskar Nagar,Patient Care
Nurses,Medilink Healthcare,9426255666,Hospital Road,IV Infusion
Insurance Agents,LIC of India,02832220260,Sanskar Nagar,Life Insurance
Insurance Agents,Bajaj Life Insurance,02067121212,RTO Relocation,Private
Insurance Agents,HDFC Life,8657510957,RTO Relocation,Life|Health
Share Brokers,Sharekhan Ltd,8069955100,Mirzapar Highway,Trading
Share Brokers,Motilal Oswal,02832255888,Sanskarnagar,Demat
Share Brokers,Angel One,8044952453,RTO Ring Road,Discount Broker
Mutual Fund Advisors,Kiran Patel,9227542850,Golden Palace,Advisor
Mutual Fund Advisors,Finnovate Financial,9998887776,Bhuj HO,Financial Planning
Financial Advisors,Abhay Joshi,9825233111,Bhuj HO,Investment
Financial Advisors,Vishva Accounting,9879512121,Station Road,Accounting|Tax
Banks,State Bank of India,02832250436,Station Road,Govt Bank
Banks,HDFC Bank,18602676161,Jubilee Circle,Private Bank
Banks,ICICI Bank,9898278000,Station Road,ATM|Branch
Banks,Bank of Baroda,02832229712,College Road,Nationalized
Website Designers,Infinitie Technologies,9879511222,Station Road,Web|App
Website Designers,WRTeam,9797945459,Time Square Empire,Software|App
Website Designers,Bigimmense IT,7417890719,Bhuj HO,SEO|Web
Pest Control,Deccan Pest Control,9666648420,Bhuj HO,Termite|Cockroach
Pest Control,Universal Pest Control,9099459608,Madhapar,Bed Bugs
Pest Control,Muskan Pest Control,9825123456,Bohra Colony,Residential
Tank Cleaning,Mannubhai Cleaning,7065012902,Bhuj HO,Tank|Sump
Tank Cleaning,Pratham Tank Cleaning,9879123456,Suncity Road,Mechanized
Restaurants,Umiyaji Dining Hall,08511186826,Station Road,Gujarati Thali
Restaurants,Viram Garden,02832250000,Sanskar Nagar,Garden|Punjabi
Restaurants,Nityanand Restaurant,02832220000,Station Road,AC|Family
Restaurants,Toral Restaurant,02832225000,Town Hall,Authentic
Hotels,Hotel Nest,7041458336,Station Road,Budget|Clean
Hotels,Click Hotel,7226933310,Station Road,Business
Hotels,Hotel White Desert,9913845450,Bhuj HO,Luxury
Homestays,Raahghar Homestays,7021819015,Bhuj Outskirts,Cultural
Homestays,Sharad Baug Homestay,02832220022,City Center,Heritage
Hospitals,MMPJ Hospital,9574230132,Bhuj HO,Emergency|24x7
Hospitals,KK Patel Super Speciality,7359007000,Bhuj HO,Multi-Speciality
Hospitals,GK General Hospital,02832250150,Lotus Colony,Govt Hospital
Hospitals,Aayush Hospitals,7573888921,Bhuj HO,Emergency
Hospitals,Om Hospital,02832255111,Hospital Road,General
Laboratories,Metropolis Healthcare,07941057323,Hospital Road,Blood Test
Laboratories,Sterling Accuris,8128130000,Lotus Colony,Diagnostics
Laboratories,Bhagat Laboratory,02832254206,Vijay Nagar,Pathology
Tank Cleaning,No Name,9879906848,9265187477,Tank Cleaning
Insurance Agents,Hiral Thacker,9879359789,Bhuj,Insurance Manager
Mutual Fund Advisors,Ashok C. Thacker,7990766093,Bhuj,Mutual Fund Advisor
Bike/Scooter Repair,Sample Garage,0000000000,Bhuj,Test
Car Mechanic,Sample Mechanic,0000000000,Bhuj,Test
Tyre/Puncture Shop,Sample Tyre,0000000000,Bhuj,Test
Inverter/Battery Dealers,Sample Battery,0000000000,Bhuj,Test
Solar Panel Installation,Sample Solar,0000000000,Bhuj,Test
Water Purifier Service,Sample RO,0000000000,Bhuj,Test
Civil Contractor,Sample Builder,0000000000,Bhuj,Test
Interior Designer,Sample Decor,0000000000,Bhuj,Test
POP/False Ceiling,Sample POP,0000000000,Bhuj,Test
Modular Kitchen,Sample Kitchen,0000000000,Bhuj,Test
Aluminium Fabrication,Sample Glass,0000000000,Bhuj,Test
Real Estate Agents,Sample Broker,0000000000,Bhuj,Test
House/Shop Rentals,Sample Rental,0000000000,Bhuj,Test
PG/Hostels,Sample PG,0000000000,Bhuj,Test
Construction Material,Sample Supplier,0000000000,Bhuj,Test
Transport/Tempo Services,Sample Transport,0000000000,Bhuj,Test
Packers & Movers,Sample Mover,0000000000,Bhuj,Test
Babysitters,Sample Care,0000000000,Bhuj,Test
Caretakers/Elder Care,Sample Care,0000000000,Bhuj,Test
Physiotherapists,Sample Physio,0000000000,Bhuj,Test
Nutritionists/Dieticians,Sample Diet,0000000000,Bhuj,Test
Yoga/Fitness Trainers,Sample Gym,0000000000,Bhuj,Test
Event Planners,Sample Event,0000000000,Bhuj,Test
Decoration Services,Sample Decor,0000000000,Bhuj,Test
Caterers,Sample Food,0000000000,Bhuj,Test
Photographer/Videographer,Sample Studio,0000000000,Bhuj,Test
CA/Tax Consultants,Sample CA,0000000000,Bhuj,Test
GST/Accounting Services,Sample Account,0000000000,Bhuj,Test
Printing & Flex Banner,Sample Print,0000000000,Bhuj,Test
Digital Marketing,Sample Agency,0000000000,Bhuj,Test
Graphic Designers,Sample Designer,0000000000,Bhuj,Test
Hardware Stores,Sample Hardware,0000000000,Bhuj,Test
Electrical Stores,Sample Electric,0000000000,Bhuj,Test
Stationery,Sample Shop,0000000000,Bhuj,Test
Courier Services,Sample Courier,0000000000,Bhuj,Test
Notary/Legal Services,Sample Advocate,0000000000,Bhuj,Test
Astrology/Vaastu,Sample Pandit,0000000000,Bhuj,Test
Tent & Sound System,Sample Sound,0000000000,Bhuj,Test
Flower Shops,Sample Florist,0000000000,Bhuj,Test
Ice Delivery,Sample Ice,0000000000,Bhuj,Test
Milk Delivery,Sample Dairy,0000000000,Bhuj,Test
Sweet Shops/Mithai,Sample Sweets,0000000000,Bhuj,Test
Cold Storage,Sample Storage,0000000000,Bhuj,Test
Jewellers,Sample Jeweller,0000000000,Bhuj,Test
Agricultural Implements,Sample Agro,0000000000,Bhuj,Test
Veterinary/Animal Care,Sample Vet,0000000000,Bhuj,Test
Ambulance,Sample Ambulance,0000000000,Bhuj,Test
Blood Bank,Sample Blood Bank,0000000000,Bhuj,Test
Fire Services,Sample Fire,0000000000,Bhuj,Test
Emergency Electrician,Sample Electrician,0000000000,Bhuj,Test
Emergency Plumber,Sample Plumber,0000000000,Bhuj,Test
Disaster Repair,Sample Repair,0000000000,Bhuj,Test
Plumber,Khenghar,9712260317,Bhuj,
Plumber,Jakhubhai,9099195439,Bhuj,
Plumber,Soni,9726946507,Bhuj,
Masons,Tejo Kadio,9909278215, 990-988-3577,
Electrician,Gadhvibhai,9664683327,,
Electrician,Kuldeep,9978222401,7567515337,
Tiles Fitter,Ravendra,9979476086,,
Tiles Fitter,Samji,9825777326,,
Tiles Fitter,Narsinhbhai,9879766942,,
Tiles Fitter,Prakashbhai,9913508113,,
Tiles Fitter,Ajaybhai,9664980323,9978392885,
Tiles Fitter,Jagdish Kumavat,9586663382,,
Tiles Fitter,Jaylila Tiles,9727726209,,
Tank Cleaning,Mukesh Goswami,7069147471,Bhuj,
Tank Cleaning,Ramesh Tank Cleaner,9978703032,Bhuj,
Water Tanker Services,Shiv Tanker Services,9825223373,Bhuj,
Electrician,Harishbhai,9725222469,Bhuj,
Laundry / Dhobi,Shahil,7359361293,,
Plumber,Kirit Maraj,9429341473,,
`;

// ----------------------------------------------------
// METADATA: Icons and Translations
// ----------------------------------------------------
const categoryMetadata = {
    // --- Core Practical Services ---
    "Electrician": { "icon": "⚡", "gu": "ઇલેક્ટ્રિશિયન" },
    "Plumber": { "icon": "🔧", "gu": "પ્લમ્બર" },
    "Carpenter": { "icon": "🪚", "gu": "સુથાર" },
    "Masons": { "icon": "🧱", "gu": "કડિયા" },
    "AC/Fridge Repair": { "icon": "❄️", "gu": "એસી/ફ્રિજ રિપેર" },
    "Refrigeration & Commercial Cooling": { "icon": "❄️", "gu": "કોમર્શિયલ કુલિંગ" },
    "Washing Machine Repair": { "icon": "🧺", "gu": "વોશિંગ મશીન રિપેર" },
    "Bike/Scooter Repair": { "icon": "🛵", "gu": "બાઈક રિપેર" },
    "Car Mechanic": { "icon": "🚗", "gu": "કાર મિકેનિક" },
    "Tyre/Puncture Shop": { "icon": "🔘", "gu": "ટાયર/પંચર" },
    "Inverter/Battery Dealers": { "icon": "🔋", "gu": "બેટરી/ઇન્વર્ટર" },
    "Solar Panel Installation": { "icon": "☀️", "gu": "સોલર પેનલ" },
    "Water Purifier Service": { "icon": "💧", "gu": "RO સર્વિસ" },
    "Civil Contractor": { "icon": "🏗️", "gu": "સિવિલ કોન્ટ્રાક્ટર" },
    "Interior Designer": { "icon": "🛋️", "gu": "ઇન્ટિરિયર ડિઝાઇનર" },
    "POP/False Ceiling": { "icon": "🏠", "gu": "POP કામ" },
    "Modular Kitchen": { "icon": "🍳", "gu": "મોડ્યુલર કિચન" },
    "Aluminium Fabrication": { "icon": "🪟", "gu": "એલ્યુમિનિયમ કામ" },
    "Tiles Fitter": { "icon": "💠", "gu": "ટાઈલ્સ ફિટર" },

    // --- Housing & Property ---
    "Real Estate Agents": { "icon": "🏘️", "gu": "રિયલ એસ્ટેટ" },
    "House/Shop Rentals": { "icon": "🔑", "gu": "ભાડે મકાન/દુકાન" },
    "PG/Hostels": { "icon": "🛏️", "gu": "PG/હોસ્ટેલ" },
    "Construction Material": { "icon": "🧱", "gu": "બાંધકામ સામગ્રી" },
    "Transport/Tempo Services": { "icon": "🚛", "gu": "ટ્રાન્સપોર્ટ/ટેમ્પો" },
    "Packers & Movers": { "icon": "📦", "gu": "પેકર્સ એન્ડ મૂવર્સ" },

    // --- Personal & Domestic ---
    "Babysitters": { "icon": "👶", "gu": "બેબીસીટર" },
    "Caretakers/Elder Care": { "icon": "👴", "gu": "વડીલ સંભાળ" },
    "Physiotherapists": { "icon": "💪", "gu": "ફિઝિયોથેરાપીસ્ટ" },
    "Nutritionists/Dieticians": { "icon": "🥗", "gu": "ડાયેટિશિયન" },
    "Yoga/Fitness Trainers": { "icon": "🧘", "gu": "યોગા/ફિટનેસ" },
    "Event Planners": { "icon": "🎉", "gu": "ઇવેન્ટ પ્લાનર" },
    "Decoration Services": { "icon": "🎈", "gu": "ડેકોરેશન" },
    "Caterers": { "icon": "🍽️", "gu": "કેટરર્સ" },
    "Photographer/Videographer": { "icon": "📸", "gu": "ફોટોગ્રાફર" },
    "Tailor": { "icon": "🧵", "gu": "દરજી" },
    "Laundry": { "icon": "👕", "gu": "લોન્ડ્રી" },
    "Laundry / Dhobi": { "icon": "👕", "gu": "લોન્ડ્રી / ધોબી" },
    "House Cleaning": { "icon": "🧹", "gu": "સફાઈ" },
    "Pest Control": { "icon": "🐜", "gu": "પેસ્ટ કંટ્રોલ" },
    "Tank Cleaning": { "icon": "🛢️", "gu": "ટાંકી સફાઈ" },
    "Gardener": { "icon": "🌱", "gu": "માળી" },

    // --- Business & Professional ---
    "CA/Tax Consultants": { "icon": "📊", "gu": "CA/ટેક્સ" },
    "GST/Accounting Services": { "icon": "📒", "gu": "GST/એકાઉન્ટિંગ" },
    "Printing & Flex Banner": { "icon": "🖨️", "gu": "પ્રિન્ટિંગ/બેનર" },
    "Digital Marketing": { "icon": "📱", "gu": "ડિજિટલ માર્કેટિંગ" },
    "Graphic Designers": { "icon": "🎨", "gu": "ગ્રાફિક ડિઝાઇનર" },
    "Hardware Stores": { "icon": "🔩", "gu": "હાર્ડવેર" },
    "Electrical Stores": { "icon": "💡", "gu": "ઇલેક્ટ્રિકલ સ્ટોર" },
    "Stationery": { "icon": "✏️", "gu": "સ્ટેશનરી" },
    "Courier Services": { "icon": "📦", "gu": "કુરિયર" },
    "Notary/Legal Services": { "icon": "⚖️", "gu": "નોટરી/વકીલ" },
    "Website Designers": { "icon": "🌐", "gu": "વેબસાઇટ ડિઝાઇનર" },
    "Insurance Agents": { "icon": "🛡️", "gu": "વીમા એજન્ટ" },
    "Share Brokers": { "icon": "📈", "gu": "શેર બ્રોકર" },
    "Mutual Fund Advisors": { "icon": "📊", "gu": "મ્યુચ્યુઅલ ફંડ" },
    "Financial Advisors": { "icon": "💰", "gu": "નાણાકીય સલાહકાર" },
    "Banks": { "icon": "🏦", "gu": "બેંક" },

    // --- Local Niche ---
    "Astrology/Vaastu": { "icon": "🔮", "gu": "જ્યોતિષ/વાસ્તુ" },
    "Tent & Sound System": { "icon": "🎪", "gu": "ટેન્ટ/સાઉન્ડ" },
    "Flower Shops": { "icon": "💐", "gu": "ફૂલવાળા" },
    "Ice Delivery": { "icon": "🧊", "gu": "બરફ" },
    "Milk Delivery": { "icon": "🥛", "gu": "દૂધ વિતરણ" },
    "Sweet Shops/Mithai": { "icon": "🍬", "gu": "મીઠાઈ" },
    "Cold Storage": { "icon": "❄️", "gu": "કોલ્ડ સ્ટોરેજ" },
    "Jewellers": { "icon": "💍", "gu": "જ્વેલર્સ" },
    "Agricultural Implements": { "icon": "🚜", "gu": "ખેતીના સાધનો" },
    "Water Tanker Services": { "icon": "💧", "gu": "પાણીના ટેન્કર" },
    "Veterinary/Animal Care": { "icon": "🐕", "gu": "પશુ સારવાર" },

    // --- Emergency Cluster ---
    "Ambulance": { "icon": "🚑", "gu": "એમ્બ્યુલન્સ" },
    "Blood Bank": { "icon": "🩸", "gu": "બ્લડ બેંક" },
    "Fire Services": { "icon": "🚒", "gu": "ફાયર બ્રિગેડ" },
    "Emergency Electrician": { "icon": "⚡", "gu": "ઈમરજન્સી ઇલેક્ટ્રિશિયન" },
    "Emergency Plumber": { "icon": "🔧", "gu": "ઈમરજન્સી પ્લમ્બર" },
    "Disaster Repair": { "icon": "🏚️", "gu": "આપત્તિ સમારકામ" },
    "Hospitals": { "icon": "🏥", "gu": "હોસ્પિટલ" },
    "Laboratories": { "icon": "🧪", "gu": "લેબોરેટરી" },
    "Medical": { "icon": "💊", "gu": "મેડિકલ સ્ટોર" },

    // --- Existing Basics ---
    "Restaurants": { "icon": "🍽️", "gu": "રેસ્ટોરન્ટ" },
    "Hotels": { "icon": "🏨", "gu": "હોટલ" },
    "Homestays": { "icon": "🏡", "gu": "હોમસ્ટે" },
    "Tuition Classes": { "icon": "📖", "gu": "ટ્યુશન ક્લાસીસ" },
    "Schools": { "icon": "🏫", "gu": "શાળા" },
    "Colleges": { "icon": "🎓", "gu": "કોલેજ" },
};

// ----------------------------------------------------
// LOGIC (Do not edit below this line)
// ----------------------------------------------------

function parseCSV(csv) {
    const lines = csv.trim().split('\n');
    const categoryMap = {};

    for (let i = 1; i < lines.length; i++) {
        const line = lines[i].trim();
        if (!line) continue;

        // Split by comma, but ignore commas inside double quotes
        // This regex matches a comma only if it is followed by an even number of quotes
        const cols = line.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/).map(c => c.trim().replace(/^"|"$/g, ''));

        const catName = cols[0];
        const name = cols[1];
        const phone = cols[2] || "";
        const area = cols[3] || "";
        const rawTags = cols[4] || "";

        if (!catName || !name) continue;

        const catId = catName.toLowerCase()
            .replace(/\//g, '-')
            .replace(/[^a-z0-9-]/g, '')
            .replace(/-+/g, '-');

        if (!categoryMap[catId]) {
            // Lookup metadata
            const meta = categoryMetadata[catName] || { "icon": "🔧", "gu": catName };

            categoryMap[catId] = {
                id: catId,
                name: catName,
                icon: meta.icon,
                gu_name: meta.gu,
                providers: []
            };
        }

        categoryMap[catId].providers.push({
            name: name,
            phone: phone,
            area: area,
            tags: rawTags ? rawTags.split('|').filter(t => t.length > 0) : []
        });
    }

    return Object.values(categoryMap);
}

// Global data initialization function
window.initializeData = async function () {
    try {
        console.log("Attempting to fetch data.csv...");
        // Add timestamp to prevent caching
        const response = await fetch(`./data.csv?v=${Date.now()}`);
        if (!response.ok) throw new Error("Network response was not ok");
        const csvText = await response.text();
        console.log("Successfully loaded data.csv from server.");
        window.bhujData = parseCSV(csvText);
    } catch (error) {
        console.log("Could not load data.csv. Using fallback data.");
        console.error(error);
        window.bhujData = parseCSV(csvRaw);
    }
};

window.getAllCategories = function () {
    return window.bhujData.map(c => ({
        id: c.id,
        name: c.name,
        icon: c.icon,
        gu_name: c.gu_name
    }));
};

window.getProviders = function (catId) {
    return window.bhujData.find(c => c.id === catId) || null;
};
