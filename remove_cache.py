import os
import glob
import re

def remove_cache_buster(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove ?v=timestamp from all image paths
    content = re.sub(r'(images/[a-zA-Z0-9_]+\.(?:png|jpg))\?v=\d+', r'\1', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

remove_cache_buster("c:\\webs\\السعودية يبويا\\style.css")

for html_file in glob.glob("c:\\webs\\السعودية يبويا\\*.html"):
    remove_cache_buster(html_file)

js_file = "c:\\webs\\السعودية يبويا\\generate_pages.js"
if os.path.exists(js_file):
    remove_cache_buster(js_file)

print("Removed cache buster from all image paths.")
