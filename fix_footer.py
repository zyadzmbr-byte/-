import os
import glob
import re

css_file = "c:\\webs\\السعودية يبويا\\style.css"

with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Make footer text bright white
css += "\n\n/* Footer Bright White and Gold */\n"
css += ".footer-engineered, .footer-engineered p, .footer-engineered h2, .footer-engineered h3, .footer-engineered li, .footer-engineered a, .footer-bottom {\n"
css += "    color: #ffffff !important;\n"
css += "}\n"

# Important words in gold
# Golden color: #FFD700 (bright gold)
css += ".footer-bottom span, strong, b {\n"
css += "    color: #FFD700 !important;\n"
css += "    text-shadow: 0 0 5px rgba(255, 215, 0, 0.4);\n"
css += "}\n"

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

# Remove social icons from HTML files
for html_file in glob.glob("c:\\webs\\السعودية يبويا\\*.html"):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove the whole social-icons div
    html = re.sub(r'<div class="social-icons".*?</div>', '', html, flags=re.DOTALL)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

# Also remove from generate_pages.js just in case
js_file = "c:\\webs\\السعودية يبويا\\generate_pages.js"
if os.path.exists(js_file):
    with open(js_file, 'r', encoding='utf-8') as f:
        js = f.read()
    js = re.sub(r'<div class="social-icons".*?</div>', '', js, flags=re.DOTALL)
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js)

print("Footer fixed: links removed, colors updated to white and gold.")
