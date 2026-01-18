import os
import datetime

BASE_URL = "https://www.bhujonline.com"

def generate_sitemap():
    sitemap_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    # Get all HTML files
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Priority rules
    # Index: 1.0
    # Main pages: 0.8
    # SEO pages (*-in-bhuj.html): 0.7
    # Others: 0.6
    
    current_date = datetime.date.today().isoformat()

    for file in files:
        if file == 'snippet.html' or file.startswith('google'):
            continue
            
        priority = "0.6"
        if file == 'index.html':
            priority = "1.0"
        elif file in ['about.html', 'category.html', 'create-webpage.html', 'haritech.html']:
            priority = "0.8"
        elif '-in-bhuj.html' in file:
            priority = "0.7"
            
        # Handle index.html as root /
        if file == 'index.html':
            loc = BASE_URL + "/"
        else:
            loc = f"{BASE_URL}/{file}"
            
        sitemap_content.append('  <url>')
        sitemap_content.append(f'    <loc>{loc}</loc>')
        sitemap_content.append(f'    <lastmod>{current_date}</lastmod>')
        sitemap_content.append(f'    <priority>{priority}</priority>')
        sitemap_content.append('  </url>')

    sitemap_content.append('</urlset>')
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sitemap_content))
        
    print(f"Generated sitemap.xml with {len(files)} URLs.")

if __name__ == "__main__":
    generate_sitemap()
