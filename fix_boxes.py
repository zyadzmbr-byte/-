import os
import glob
import re

# 1. Update style.css
css_file = "c:\\webs\\السعودية يبويا\\style.css"
if os.path.exists(css_file):
    with open(css_file, 'r', encoding='utf-8') as f:
        css = f.read()

    # Boxes with images (acc-body, blog-post, content-card if it's there)
    css = re.sub(r'(\.acc-body\s*\{[^}]*)', lambda m: m.group(1).replace('background-color: var(--bg-card);', 'background-color: #111111; color: #ffffff;') if 'background' in m.group(1) else m.group(1) + ' background-color: #111111; color: #ffffff;', css)
    
    css += "\n\n/* Added for white text in boxes with images */\n"
    css += ".acc-body, .blog-post, .content-card, .service-details, .acc-info {\n"
    css += "    background-color: #111111 !important;\n"
    css += "    color: #ffffff !important;\n"
    css += "}\n"
    
    css += ".acc-info h4, .acc-info p, .acc-info h5, .acc-info li, .img-caption {\n"
    css += "    color: #f5f5f5 !important;\n"
    css += "}\n"
    
    css += ".blog-post h3, .blog-post h4, .blog-post p, .blog-post li, .blog-post strong {\n"
    css += "    color: #f5f5f5 !important;\n"
    css += "}\n"

    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Update all HTML inline styles
for html_file in glob.glob("c:\\webs\\السعودية يبويا\\*.html"):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Content-card
    html = re.sub(r'(\.content-card\s*\{[^}]*background:\s*)var\(--bg-dark\)(;[^}]*\})', r'\g<1>#111111\2', html)
    html = re.sub(r'(\.content-card\s*\{[^}]*\}|(?<=.content-card \{))', lambda m: m.group(0).replace('}', ' color: #ffffff; }'), html)
    
    html = re.sub(r'(\.content-card\s+h2\s*\{[^}]*color:\s*)var\(--primary\)(;[^}]*\})', r'\g<1>#ffffff\2', html)
    html = re.sub(r'(\.content-card\s+p\s*\{[^}]*color:\s*)var\(--text-main\)(;[^}]*\})', r'\g<1>#f5f5f5\2', html)
    html = re.sub(r'(\.content-list\s+li\s*\{[^}]*color:\s*)var\(--text-main\)(;[^}]*\})', r'\g<1>#f5f5f5\2', html)
    html = re.sub(r'(\.content-list\s+strong\s*\{[^}]*color:\s*)var\(--secondary\)(;[^}]*\})', r'\g<1>#ffffff\2', html)
    
    # Also add a catch-all in the style tag if it exists
    if '<style>' in html:
        html = html.replace('</style>', ' .content-card, .content-card p, .content-card h2, .content-list li, .content-list strong { color: #ffffff !important; } .content-card { background-color: #111111 !important; } </style>')
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Text inside boxes changed to white.")
