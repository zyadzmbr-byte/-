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

tan1_b64 = get_base64_image(os.path.join(images_dir, "tan 1.jpg"))
tan21_b64 = get_base64_image(os.path.join(images_dir, "tan 2.1.jpg"))
tan22_b64 = get_base64_image(os.path.join(images_dir, "tan 2.2.jpg"))
tan3_b64 = get_base64_image(os.path.join(images_dir, "tan 3.jpg"))
tan4_b64 = get_base64_image(os.path.join(images_dir, "tan 4.jpg"))

def replace_with_b64(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace original images
    content = re.sub(r'images/bg1\.jpg', bg1_b64, content)
    content = re.sub(r'images/bg2\.jpg', bg2_b64, content)
    content = re.sub(r'images/core_drilling\.png', core_drilling_b64, content)
    content = re.sub(r'images/concrete_saw\.png', concrete_saw_b64, content)

    # Replace tan images (handle spaces in regex properly or just use strings)
    # Since re.sub interprets strings, spaces are just spaces, but dots must be escaped
    content = re.sub(r'images/tan 1\.jpg', tan1_b64, content)
    content = re.sub(r'images/tan 2\.1\.jpg', tan21_b64, content)
    content = re.sub(r'images/tan 2\.2\.jpg', tan22_b64, content)
    content = re.sub(r'images/tan 3\.jpg', tan3_b64, content)
    content = re.sub(r'images/tan 4\.jpg', tan4_b64, content)

    # Force style.css reload if it's an HTML file
    if filepath.endswith('.html'):
        content = re.sub(r'href="style\.css[^\"]*"', f'href="style.css?v={int(time.time())}"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replace_with_b64("c:\\webs\\السعودية يبويا\\style.css")

for html_file in glob.glob("c:\\webs\\السعودية يبويا\\*.html"):
    replace_with_b64(html_file)

print("Images embedded as base64 and CSS cache busted.")
