import base64
import os
import glob
import re
import time

def get_base64_image(filepath):
    with open(filepath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    ext = os.path.splitext(filepath)[1][1:] # get extension without dot
    if ext == 'jpg':
        ext = 'jpeg'
    return f"data:image/{ext};base64,{encoded_string}"

images_dir = "c:\\webs\\السعودية يبويا\\images"
bg1_b64 = get_base64_image(os.path.join(images_dir, "bg1.jpg"))
bg2_b64 = get_base64_image(os.path.join(images_dir, "bg2.jpg"))
core_drilling_b64 = get_base64_image(os.path.join(images_dir, "core_drilling.png"))
concrete_saw_b64 = get_base64_image(os.path.join(images_dir, "concrete_saw.png"))

def replace_with_b64(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace bg1.jpg
    content = re.sub(r'images/bg1\.jpg', bg1_b64, content)
    # Replace bg2.jpg
    content = re.sub(r'images/bg2\.jpg', bg2_b64, content)
    # Replace core_drilling.png
    content = re.sub(r'images/core_drilling\.png', core_drilling_b64, content)
    # Replace concrete_saw.png
    content = re.sub(r'images/concrete_saw\.png', concrete_saw_b64, content)

    # Force style.css reload if it's an HTML file
    if filepath.endswith('.html'):
        content = re.sub(r'href="style\.css[^\"]*"', f'href="style.css?v={int(time.time())}"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replace_with_b64("c:\\webs\\السعودية يبويا\\style.css")

for html_file in glob.glob("c:\\webs\\السعودية يبويا\\*.html"):
    replace_with_b64(html_file)

print("Images embedded as base64 and CSS cache busted.")
