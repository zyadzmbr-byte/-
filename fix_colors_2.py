import re

css_file = "c:\\webs\\السعودية يبويا\\style.css"

with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix .brand-text h1 color to #000 (black on white header)
css = re.sub(r'(\.brand-text\s+h1\s*\{[^}]*color:\s*)#fff(;.*?\})', r'\g<1>#000\2', css)

# 2. Fix mobile-menu a background to light gray, text to black
css = re.sub(r'(\.mobile-menu\s+a\s*\{[^}]*background:\s*)rgba\(0, 0, 0, 0\.3\)(;.*?\})', r'\g<1>#f5f5f5\2', css)
css = re.sub(r'(\.mobile-menu\s+a\s*\{[^}]*)', lambda m: m.group(0) + ' color: #000;', css, count=1)

# 3. Dropdown-content duplicate fix
css = css.replace('background-color: #fff; border: 1px solid #ddd;', '')
css = re.sub(r'\.dropdown-content\s*\{', '.dropdown-content {\n    background-color: #ffffff;', css)

# 4. .inner-hero has background var(--bg-dark), text color #000, but in HTML it might have been inline.
# inner-hero h1 was #fff, let's make it #000
css = re.sub(r'(\.inner-hero\s+h1\s*\{[^}]*color:\s*)#000000(;.*?\})', r'\g<1>#000\2', css)
css = re.sub(r'(\.inner-hero\s+h1\s*\{[^}]*color:\s*)#fff(;.*?\})', r'\g<1>#000\2', css)

# 5. Fix hero description color just in case (black text on white overlay is good, but let's ensure it's bold/clear)
css = re.sub(r'(\.hero-desc\s*\{[^}]*color:\s*)var\(--text-muted\)(;.*?\})', r'\g<1>#333\2', css)

# 6. footer-desc color to #fff (since footer bg is now #000)
css = re.sub(r'(\.footer-desc\s*\{[^}]*color:\s*)var\(--text-muted\)(;.*?\})', r'\g<1>#ccc\2', css)
css = re.sub(r'(\.footer-links\s+li\s*\{[^}]*color:\s*)var\(--text-main\)(;.*?\})', r'\g<1>#fff\2', css)
css = re.sub(r'(\.footer-links\s+a\s*\{[^}]*color:\s*)var\(--text-main\)(;.*?\})', r'\g<1>#fff\2', css)
css = re.sub(r'(\.footer-bottom\s*\{[^}]*color:\s*)var\(--text-muted\)(;.*?\})', r'\g<1>#ccc\2', css)
css = re.sub(r'(\.footer-brand\s+h2\s*\{[^}]*color:\s*)#fff(;.*?\})', r'\g<1>#fff\2', css)
# If .footer-brand h2 was black, make it white
css = re.sub(r'(\.footer-brand\s+h2\s*\{[^}]*color:\s*)#000(;.*?\})', r'\g<1>#fff\2', css)

# 7. Make sure all instances of `color: #000000;` or `color: #000;` inside dark backgrounds are fixed
# But footer is #000, so any text there should be #fff
# Let's just add color: #fff to .footer-engineered and its children
css = css.replace('.footer-engineered {', '.footer-engineered {\n    color: #fff;')
css = re.sub(r'\.footer-engineered\s+a\s*\{[^}]*\}', '', css)
css += '\n.footer-engineered a { color: #fff; }\n'

# 8. Check floating phones
# floating-phone bg should be primary (black), text white
css = re.sub(r'(\.floating-phone\s*\{[^}]*color:\s*)#fff(;.*?\})', r'\g<1>#fff\2', css)
css = re.sub(r'(\.floating-whatsapp\s*\{[^}]*color:\s*)#fff(;.*?\})', r'\g<1>#fff\2', css)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed second pass.")
