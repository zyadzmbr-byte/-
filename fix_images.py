import os
import glob
import re

def replace_images_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pexels image 1 -> images/bg1.jpg
    content = re.sub(r'https://images\.pexels\.com/photos/159306/[^\'"]+', 'images/bg1.jpg', content)
    
    # Pexels image 2 -> images/bg2.jpg
    content = re.sub(r'https://images\.pexels\.com/photos/1216589/[^\'"]+', 'images/bg2.jpg', content)
    
    # Unsplash image -> images/bg2.jpg
    content = re.sub(r'https://images\.unsplash\.com/photo-1503387762-[^\'"]+', 'images/bg2.jpg', content)
    
    # Also in style.css they might be url('https://...')
    # But since we just regexed the URL itself, it will become url('images/bg1.jpg') which is correct relative to style.css

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Update CSS
replace_images_in_file("c:\\webs\\السعودية يبويا\\style.css")

# Update all HTML files
for html_file in glob.glob("c:\\webs\\السعودية يبويا\\*.html"):
    replace_images_in_file(html_file)

# Update generate_pages.js
js_file = "c:\\webs\\السعودية يبويا\\generate_pages.js"
if os.path.exists(js_file):
    replace_images_in_file(js_file)

print("External images replaced with local images.")
