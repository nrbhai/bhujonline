import csv
import os
import re
import html

# Template for the static page
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-FM47B49F2S"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());

      gtag('config', 'G-FM47B49F2S');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css?v=1768722344">
    <style>
        /* Additional SEO page styles if needed */
        .provider-card {{ display: flex; flex-direction: column; gap: 8px; }}
        .badges {{ display: flex; gap: 5px; margin-bottom: 5px; }}
        .badge {{ padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }}
        .badge.verified {{ background: #e0f2fe; color: #0284c7; }}
        .badge.top-rated {{ background: #fef3c7; color: #d97706; }}
        .provider-header {{ display: flex; justify-content: space-between; align-items: flex-start; }}
        .provider-name {{ font-weight: bold; font-size: 1.1rem; color: #1f2937; }}
        .provider-meta {{ display: flex; flex-direction: column; gap: 4px; color: #4b5563; font-size: 0.95rem; }}
        .provider-actions {{ display: flex; gap: 10px; margin-top: 10px; }}
        .btn-call {{ flex: 1; text-align: center; background: #f3f4f6; color: #1f2937; padding: 8px; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 0.9rem; }}
        .btn-call.primary {{ background: #eff6ff; color: #2563eb; }}
    </style>
</head>
<body>
    <div class="container">
        <header style="flex-direction: column; text-align: center; gap: 0;">
            <a href="index.html" style="text-decoration: none; color: inherit;">
                <img src="assets/public/images/bhujonline-logo.png" alt="Bhuj Online Logo" style="height: 250px; width: auto; display: block; margin: 0 auto 5px auto;">
            </a>
        </header>

        <main>
            <a href="index.html" class="back-link">← Back to Categories</a>
            
            <h1 style="margin-bottom: 10px; font-size: 1.5rem; color: #111827;">{heading}</h1>
            <p style="color: #6b7280; margin-bottom: 20px;">Find the best {category_name} in Bhuj. Verified contact numbers and reviews.</p>
            
            <ul class="provider-list">
                {content}
            </ul>
        </main>


        <footer>
            <p>Made for Bhuj by Hari Tech Solutions ! Ph : 9512234395</p>
            <div style="margin-top: 10px; font-size: 0.9rem;">
                <a href="index.html" style="color: #4b5563;">Home</a> | 
                <a href="about.html" style="color: #4b5563;">About</a>
            </div>
        </footer>
    </div>
</body>
</html>"""

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def generate_pages():
    categories = {}
    
    # Read CSV
    with open('data.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row['Category'].strip()
            if cat:
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(row)

    generated_files = []

    # Generate pages
    for cat, providers in categories.items():
        slug = slugify(cat)
        filename = f"{slug}-in-bhuj.html"
        
        # Sort providers: Verified + Top Rated first, then Verified, then others
        def sort_key(p):
            verified = p.get('Verified', '').strip().lower() == 'yes'
            top_rated = p.get('Top Rated', '').strip().lower() == 'yes'
            return (not (verified and top_rated), not verified)
            
        providers.sort(key=sort_key)
        
        list_html = ""
        for p in providers:
            name = html.escape(p['Name'])
            phone = p['Phone'].strip()
            area = html.escape(p['Area'])
            tags = html.escape(p['Tags'])
            webpage = p.get('Webpage', '').strip()
            verified = p.get('Verified', '').strip().lower() == 'yes'
            top_rated = p.get('Top Rated', '').strip().lower() == 'yes'
            
            badges_html = ""
            if verified: badges_html += '<span class="badge verified">Verified</span>'
            if top_rated: badges_html += '<span class="badge top-rated">Top Rated</span>'
            
            badges_div = f'<div class="badges">{badges_html}</div>' if badges_html else ''
            
            # Determine link
            name_link = name
            if webpage:
                name_link = f'<a href="{webpage}" style="color: inherit; text-decoration: none;">{name}</a>'
            
            actions_html = f'<a href="tel:{phone}" class="btn-call primary">📞 {phone}</a>'
            if webpage:
                actions_html += f'<a href="{webpage}" class="btn-call">🌐 Visit Website</a>'
                
            list_html += f"""
            <li class="provider-card" style="list-style: none; background: white; padding: 16px; border-radius: 12px; border: 1px solid #e5e7eb; margin-bottom: 12px; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
                {badges_div}
                <div class="provider-header">
                    <span class="provider-name">{name_link}</span>
                </div>
                <div class="provider-meta">
                    <span>📍 {area}</span>
                    <span style="font-size: 0.85rem; color: #9ca3af;">{tags}</span>
                </div>
                <div class="provider-actions">
                    {actions_html}
                </div>
            </li>
            """
            
        page_html = TEMPLATE.format(
            title=f"Best {cat} in Bhuj - Verified {cat} Near Me | BhujOnline",
            description=f"Find the best {cat} in Bhuj. Verified {cat} contact numbers, reviews, and address. Search reputable {cat} near you on BhujOnline.",
            heading=f"{cat} in Bhuj",
            category_name=cat,
            content=list_html
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page_html)
        
        generated_files.append({'name': cat, 'file': filename})
        # print(f"Generated {filename}")

    return generated_files

if __name__ == "__main__":
    files = generate_pages()
    
    # Generate partial HTML for homepage links
    popular_html = '<div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #e5e7eb;">'
    popular_html += '<h3 style="font-size: 1.2rem; margin-bottom: 15px;">Popular Services in Bhuj</h3>'
    popular_html += '<div style="display: flex; flex-wrap: wrap; gap: 10px;">'
    
    for item in files:
        popular_html += f'<a href="{item["file"]}" style="font-size: 0.9rem; color: #4b5563; text-decoration: none; background: #f3f4f6; padding: 4px 10px; border-radius: 15px;">{item["name"]}</a>'
    
    popular_html += '</div></div>'
    
    with open('snippet.html', 'w', encoding='utf-8') as f:
        f.write(popular_html)
    print("Snippet written to snippet.html")
