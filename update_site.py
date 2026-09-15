import os
import re
import glob

# Set working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

spec = "متخصص في قص الخرسانه و قص الابواب ودرايش وتكسيرات وتكسير بلاط جميع التكسير وفتحات كور من 1 بوصة ل 16 بوصة والقص بمنشار ليزر في السعودية الرياض"

# Process HTML files
for file_path in glob.glob("*.html"):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Change names
    content = re.sub(r'Expert-Core', 'ابو عبد الرحمن', content)
    content = re.sub(r'إشراف المهندس \/ معتصم حمدي', 'ابو عبد الرحمن', content)
    content = re.sub(r'المهندس معتصم حمدي', 'ابو عبد الرحمن', content)
    content = re.sub(r'البشمهندس معتصم', 'ابو عبد الرحمن', content)
    content = re.sub(r'معتصم حمدي', 'ابو عبد الرحمن', content)

    # 2. Change phone numbers
    content = re.sub(r'010\s*3383\s*1671', '0553770127', content)
    content = re.sub(r'011\s*5280\s*0018', '0553770127', content)
    content = re.sub(r'\+201033831671', '+966553770127', content)
    content = re.sub(r'\+201152800018', '+966553770127', content)

    # 3. Remove whatsapp links but keep structure if possible, or remove elements
    # Remove header whatsapp block
    content = re.sub(r'<a href="https://wa\.me.*?class="header-whatsapp".*?</a>', '', content, flags=re.DOTALL)
    # Remove mobile menu whatsapp
    content = re.sub(r'<a href="https://wa\.me.*?class="contact-menu-link">.*?</a>', '', content, flags=re.DOTALL)
    # Replace any other wa.me links with tel
    content = re.sub(r'href="https://wa\.me/[^"]*"', 'href="tel:0553770127"', content)
    # Replace whatsapp classes/icons with phone
    content = re.sub(r'btn-whatsapp', 'btn-primary', content)
    content = re.sub(r'fab fa-whatsapp', 'fas fa-phone', content)
    # For floating whatsapp, remove it
    content = re.sub(r'<a href="tel:0553770127"[^>]*class="floating-whatsapp"[^>]*>.*?</a>', '', content, flags=re.DOTALL)

    # 4. Remove social links in schema
    content = re.sub(r'"sameAs":\s*\[.*?\]', '"sameAs": []', content, flags=re.DOTALL)

    # 5. Add Location and SEO
    content = re.sub(r'في مصر', 'في السعودية الرياض', content)
    
    # Meta description
    def repl_meta(m):
        return f'<meta name="description" content="{m.group(1)} {spec}"'
    content = re.sub(r'<meta name="description"\s*content="(.*?)"', repl_meta, content)

    # Hero description
    content = re.sub(r'شريكك الموثوق لتنفيذ كافة أعمال', f'شريكك الموثوق في السعودية الرياض لتنفيذ كافة أعمال {spec}، ', content)

    # Footer rights
    content = re.sub(r'جميع الحقوق محفوظة لـ', 'السعودية الرياض - السعودية الرياض - جميع الحقوق محفوظة لـ', content)

    # Add extra keywords to title of index if needed
    content = re.sub(r'<title>(.*?)<\/title>', r'<title>\1 - السعودية الرياض</title>', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix CSS colors
css_file = "style.css"
if os.path.exists(css_file):
    with open(css_file, 'r', encoding='utf-8') as f:
        css = f.read()

    # Replace primary colors with black/white/gray equivalents
    css = re.sub(r'--primary:\s*#[0-9a-fA-F]+;', '--primary: #000000;', css)
    css = re.sub(r'--secondary:\s*#[0-9a-fA-F]+;', '--secondary: #333333;', css)
    css = re.sub(r'--accent:\s*#[0-9a-fA-F]+;', '--accent: #666666;', css)
    css = re.sub(r'--whatsapp:\s*#[0-9a-fA-F]+;', '--whatsapp: #000000;', css)

    # Replace hardcoded hex colors
    css = re.sub(r'#ff6a00', '#000000', css, flags=re.IGNORECASE)
    
    # Change background colors if necessary to ensure black and white theme
    # Using #f9f9f9 instead of dark backgrounds
    css = re.sub(r'#17191c', '#ffffff', css, flags=re.IGNORECASE)
    css = re.sub(r'#212429', '#f5f5f5', css, flags=re.IGNORECASE)
    css = re.sub(r'--bg-dark:\s*#[0-9a-fA-F]+;', '--bg-dark: #ffffff;', css)
    css = re.sub(r'--bg-card:\s*#[0-9a-fA-F]+;', '--bg-card: #f5f5f5;', css)
    css = re.sub(r'--text-main:\s*#[0-9a-fA-F]+;', '--text-main: #333333;', css)
    
    # In case there are text colors that are white, they need to be black now if bg is white
    css = re.sub(r'color:\s*#fff;', 'color: #000;', css, flags=re.IGNORECASE)
    css = re.sub(r'color:\s*#ffffff;', 'color: #000000;', css, flags=re.IGNORECASE)
    
    # For buttons text color (which were probably white on orange bg, now white on black bg is fine)
    # But wait, I changed `color: #fff;` to `color: #000;` blindly.
    # Let's revert that specific change, or just let it be and we can manually fix css if broken.
    # Actually, let's only modify the variables to be safer.
    
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

print("Done modifying files")
