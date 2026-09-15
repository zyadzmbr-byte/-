import os
import glob
import re
import time

timestamp = str(int(time.time()))

def bypass_cache_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add ?v=timestamp to all images/...png and images/...jpg
    # Only if they don't already have ?v=
    content = re.sub(r'(images/[a-zA-Z0-9_]+\.(?:png|jpg))(?![\?])', r'\1?v=' + timestamp, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

bypass_cache_in_file("c:\\webs\\السعودية يبويا\\style.css")

for html_file in glob.glob("c:\\webs\\السعودية يبويا\\*.html"):
    bypass_cache_in_file(html_file)

js_file = "c:\\webs\\السعودية يبويا\\generate_pages.js"
if os.path.exists(js_file):
    bypass_cache_in_file(js_file)

print("Added cache buster to all image paths.")
