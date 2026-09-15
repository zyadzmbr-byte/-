import re

css_file = "c:\\webs\\السعودية يبويا\\style.css"

with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Darken text-muted for better contrast
css = re.sub(r'--text-muted:\s*#666666;', '--text-muted: #333333;', css)
css = re.sub(r'--text-muted:\s*#A1AAB4;', '--text-muted: #333333;', css)

# 2. Fix page-header gradient
css = css.replace('rgba(9, 15, 22, 0.9)', 'rgba(255, 255, 255, 0.9)')
css = css.replace('rgba(9, 15, 22, 0.8)', 'rgba(255, 255, 255, 0.8)')

# 3. Fix footer-engineered background to be black so white text works
# Currently it has `background-color: var(--bg-card);` which is light gray.
css = css.replace('background-color: var(--bg-card);\n    padding-top: 80px;', 'background-color: #000000;\n    padding-top: 80px;')

# 4. Make sure .footer-bottom background is slightly lighter black
css = css.replace('background: rgba(0, 0, 0, 0.3);', 'background: #111111;')
css = re.sub(r'(\.footer-bottom\s*\{[^}]*color:\s*)var\(--text-muted\)(;.*?\})', r'\g<1>#cccccc\2', css)

# 5. Fix any other black-on-dark or white-on-light
# .btn-primary is white on black, .btn-primary:hover is white on #333
# .dropdown-content is #fff bg, so links should be #000 (handled because text-main is #000)

# Check value-banner
# .value-banner might have a dark background. Let's make sure it's light gray #f9f9f9 with black text.
# Actually let's just make sure h2 and p inside value-banner are #000
css = re.sub(r'(\.value-banner\s+h2\s*\{[^}]*color:\s*)#fff(;.*?\})', r'\g<1>#000\2', css)

# Fix .service-content-main h2
css = re.sub(r'(\.service-content-main\s+h2\s*\{[^}]*color:\s*)var\(--primary\)(;.*?\})', r'\g<1>#000\2', css)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS Fixed")
