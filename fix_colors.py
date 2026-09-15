import os
import re

css_file = "c:\\webs\\السعودية يبويا\\style.css"

with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix CSS Variables
css = re.sub(r'--primary-hover:\s*#E05D00;', '--primary-hover: #333333;', css)
css = re.sub(r'--border-color:\s*#[0-9A-Fa-f]+;', '--border-color: #dddddd;', css)
css = re.sub(r'--text-muted:\s*#[0-9A-Fa-f]+;', '--text-muted: #666666;', css)
css = re.sub(r'--shadow:\s*0\s+10px\s+30px\s+rgba\(0,\s*0,\s*0,\s*0\.5\);', '--shadow: 0 10px 30px rgba(0, 0, 0, 0.1);', css)

# Fix rgba backgrounds that were dark
css = re.sub(r'background-color:\s*rgba\(9,\s*15,\s*22,\s*0\.95\);', 'background-color: rgba(255, 255, 255, 0.95);', css)
css = re.sub(r'background:\s*rgba\(13,\s*22,\s*32,\s*0\.85\);', 'background: rgba(255, 255, 255, 0.85);', css)
css = re.sub(r'background:\s*rgba\(255,\s*255,\s*255,\s*0\.05\);', 'background: rgba(0, 0, 0, 0.05);', css)

# Fix any hardcoded orange or blue rgba
css = re.sub(r'rgba\(255,\s*106,\s*0,\s*([0-9.]+)\)', r'rgba(0, 0, 0, \1)', css)

# Fix any remaining black text on dark background by ensuring dark backgrounds are light
# For example footer
css = re.sub(r'\.footer-engineered\s*{[^}]*}', lambda m: m.group(0).replace('background: var(--bg-dark);', 'background: #f1f1f1;'), css)

# Fix box-shadows with orange
css = re.sub(r'box-shadow:\s*0\s+4px\s+15px\s+rgba\(255,\s*106,\s*0,\s*0\.3\);', 'box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);', css)
css = re.sub(r'box-shadow:\s*0\s+8px\s+25px\s+rgba\(255,\s*106,\s*0,\s*0\.5\);', 'box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);', css)
css = re.sub(r'box-shadow:\s*0\s+10px\s+30px\s+rgba\(255,\s*106,\s*0,\s*0\.2\);', 'box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);', css)
css = re.sub(r'box-shadow:\s*0\s+0\s+20px\s+rgba\(255,\s*106,\s*0,\s*0\.4\);', 'box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);', css)

# Button text was black, btn-primary background is black. So black on black!
# Let's fix btn-primary to have white text on black background
# Original code:
# .btn-primary { background-color: var(--primary); color: #000; }
# Let's change `color: #000;` inside `.btn-primary` and others where background is primary
css = re.sub(r'\.btn-primary\s*{[^}]*color:\s*#000;[^}]*}', lambda m: m.group(0).replace('color: #000;', 'color: #fff;'), css)

# WhatsApp button was changed to btn-primary but let's make sure its color is white if background is black
css = re.sub(r'\.btn-whatsapp\s*{[^}]*color:\s*#000;[^}]*}', lambda m: m.group(0).replace('color: #000;', 'color: #fff;'), css)

# Header icons and hover states
css = re.sub(r'\.icon-circle\s*{[^}]*color:\s*#000;[^}]*}', lambda m: m.group(0).replace('color: #000;', 'color: #fff;').replace('background: rgba(0, 0, 0, 0.05);', 'background: #000;'), css)
# Actually `.icon-circle` had `color: var(--primary)` which is #000. So it was black on #000.05 (light grey). That's fine. 
# But let's just rewrite the `.btn-primary`, `.btn-whatsapp`, `.btn-outline` text colors properly
def fix_btn_colors(css_content):
    css_content = re.sub(r'(\.btn-primary\s*\{.*?color:\s*)#000(;.*?\})', r'\g<1>#fff\2', css_content, flags=re.DOTALL)
    css_content = re.sub(r'(\.btn-whatsapp\s*\{.*?color:\s*)#000(;.*?\})', r'\g<1>#fff\2', css_content, flags=re.DOTALL)
    return css_content

css = fix_btn_colors(css)

# Let's revert all instances of `color: #000;` inside elements where they were previously white, 
# wait I don't have the previous file. Let's just fix specific contrast issues:
# 1. Hero text: 
# .hero-heading was white (now #000). On a white overlay it's readable. But hero-overlay is now white.
# .hero-desc was light grey (now #000).
# .hero-badge was something else.
# So if overlay is rgba(255, 255, 255, 0.85), black text is perfect.
# But if it's on a dark image, maybe the image looks weird under white overlay.
# The user said "الاسود شفاف وباهت" (black is transparent and faded) and "الابيض مش متناسق" (white is not coordinated).
# This might mean my RGBA colors were wrong, or they saw #333333 and it looked faded.
css = re.sub(r'--secondary:\s*#333333;', '--secondary: #000000;', css)
css = re.sub(r'--text-main:\s*#333333;', '--text-main: #000000;', css)

# Let's fix `.footer-engineered`
css = re.sub(r'\.footer-engineered\s*{[^}]*}', lambda m: m.group(0).replace('background-color: var(--bg-dark);', 'background-color: #000; color: #fff;'), css)

# Make sure brand text is black
css = re.sub(r'\.brand-text\s+h1\s*{[^}]*color:\s*#000000;[^}]*}', lambda m: m.group(0).replace('#000000', '#000'), css)

# What about dropdowns?
css = re.sub(r'\.dropdown-content\s*{[^}]*}', lambda m: m.group(0).replace('background-color: var(--bg-card);', 'background-color: #fff; border: 1px solid #ddd;'), css)

# And footer titles
css = re.sub(r'\.footer-title\s*{[^}]*color:\s*#000;[^}]*}', lambda m: m.group(0).replace('color: #000;', 'color: #fff;'), css)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS Fixed")
