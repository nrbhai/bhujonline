import os
import re
import time

def update_version_in_files():
    # Get current timestamp for versioning
    timestamp = int(time.time())
    version_param = f"?v={timestamp}"
    
    # List of files to update
    files_to_update = [
        'index.html',
        'about.html',
        'haritech.html',
        'create-webpage.html',
        # Add other HTML files if needed
    ]
    
    # Also find all other .html files in root
    for file in os.listdir('.'):
        if file.endswith('.html') and file not in files_to_update:
            files_to_update.append(file)
            
    print(f"Updating version to {version_param} in {len(files_to_update)} files...")

    # Patterns to match standardized asset links
    # Matches href="...style.css" or href="...style.css?v=..."
    css_pattern = re.compile(r'(href=["\'].*?\.css)(\?v=\d+)?(["\'])')
    # Matches src="...script.js" or src="...script.js?v=..."
    js_pattern = re.compile(r'(src=["\'].*?\.js)(\?v=\d+)?(["\'])')

    for file_path in files_to_update:
        if not os.path.exists(file_path):
            print(f"Skipping {file_path} (not found)")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update CSS links
        new_content = css_pattern.sub(rf'\1{version_param}\3', content)
        
        # Update JS links
        new_content = js_pattern.sub(rf'\1{version_param}\3', new_content)
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[OK] Updated {file_path}")
        else:
            print(f"[No Change] {file_path}")

if __name__ == "__main__":
    update_version_in_files()
