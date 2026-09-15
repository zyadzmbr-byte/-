import re
import os

css_file = "c:\\webs\\السعودية يبويا\\style.css"

with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Revert page-header background gradient to dark
css = css.replace('rgba(255, 255, 255, 0.9)', 'rgba(9, 15, 22, 0.9)')
css = css.replace('rgba(255, 255, 255, 0.8)', 'rgba(9, 15, 22, 0.8)')
# (Except for .main-header which might be rgba(255, 255, 255, 0.95), let's be careful. The replacement above matches 0.9 and 0.8 exact, main-header is 0.95 so it's safe.)

# 2. Revert hero-overlay to dark
css = css.replace('background: rgba(255, 255, 255, 0.85);', 'background: rgba(13, 22, 32, 0.85);')

# 3. Ensure accordion-services overlay is dark
css = re.sub(r'(\.accordion-services::before\s*\{[^}]*background:\s*)rgba\(255, 255, 255, 0.9\)(;.*?\})', r'\g<1>rgba(9, 15, 22, 0.9)\2', css)
css = re.sub(r'(\.accordion-services::before\s*\{[^}]*background:\s*)rgba\(255, 255, 255, 0.95\)(;.*?\})', r'\g<1>rgba(9, 15, 22, 0.95)\2', css)

# 4. Enforce bright white text in these sections
css += "\n\n/* Added for bright white text on image backgrounds */\n"
css += ".hero-section, .hero-section h2, .hero-section p, .hero-heading, .hero-desc, .hero-badge {\n"
css += "    color: #ffffff !important;\n"
css += "}\n"

css += ".page-header, .page-header h1, .page-header p, .page-title, .breadcrumb, .breadcrumb a {\n"
css += "    color: #ffffff !important;\n"
css += "}\n"

# For accordion-services header (the section subtitle and intro on the background image)
css += ".accordion-services > .container > .text-center h3, \n"
css += ".accordion-services > .container > .text-center h4, \n"
css += ".accordion-services > .container > .text-center p {\n"
css += "    color: #ffffff !important;\n"
css += "}\n"

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

# Also check html inline styles for .inner-hero
for html_file in os.listdir("c:\\webs\\السعودية يبويا"):
    if html_file.endswith('.html'):
        path = os.path.join("c:\\webs\\السعودية يبويا", html_file)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Change inner-hero text to white and background to dark so it looks good
        html = re.sub(r'(\.inner-hero\s*\{[^}]*background:\s*)var\(--bg-dark\)(;.*?\})', r'\g<1>#111111\2', html)
        html = re.sub(r'(\.inner-hero\s+h1\s*\{[^}]*color:\s*)#000(;.*?\})', r'\g<1>#ffffff\2', html)
        html = re.sub(r'(\.inner-hero\s+h1\s*\{[^}]*color:\s*)#000000(;.*?\})', r'\g<1>#ffffff\2', html)

        # Make sure value banner (last section) is also dark with white text if it has an image or is "last section"
        # .value-banner { background: url(...) or solid dark? Let's make it solid dark if they want it like that
        html = re.sub(r'(\.value-banner\s*\{[^}]*background:\s*).*?(;.*?\})', r'\g<1>#111111\2', html)
        html = re.sub(r'(\.value-banner\s+h2\s*\{[^}]*color:\s*)#000(?:000)?(;.*?\})', r'\g<1>#ffffff\2', html)
        html = re.sub(r'(\.value-banner\s+p\s*\{[^}]*color:\s*)var\(--text-muted\)(;.*?\})', r'\g<1>#f5f5f5\2', html)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

print("Backgrounds and text colors fixed.")
