const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir);

const htmlFiles = files.filter(f => f.endsWith('.html'));
const cssFile = path.join(dir, 'style.css');

htmlFiles.forEach(file => {
    let content = fs.readFileSync(path.join(dir, file), 'utf8');

    // 1. Change names
    content = content.replace(/Expert-Core/g, 'ابو عبد الرحمن');
    content = content.replace(/إشراف المهندس \/ معتصم حمدي/g, 'ابو عبد الرحمن');
    content = content.replace(/المهندس معتصم حمدي/g, 'ابو عبد الرحمن');
    content = content.replace(/البشمهندس معتصم/g, 'ابو عبد الرحمن');
    content = content.replace(/معتصم حمدي/g, 'ابو عبد الرحمن');
    
    // 2. Change phone numbers
    content = content.replace(/010\s*3383\s*1671/g, '0553770127');
    content = content.replace(/01033831671/g, '0553770127');
    content = content.replace(/011\s*5280\s*0018/g, '0553770127');
    content = content.replace(/01152800018/g, '0553770127');
    content = content.replace(/\+201033831671/g, '+966553770127');
    content = content.replace(/\+201152800018/g, '+966553770127');

    // 3. Remove whatsapp icons and links
    // Floating whatsapp
    content = content.replace(/<a href="https:\/\/wa\.me.*?class="floating-whatsapp".*?<\/a>/gs, '');
    // Header whatsapp
    content = content.replace(/<a href="https:\/\/wa\.me.*?class="header-whatsapp".*?<\/a>/gs, '');
    // Mobile menu whatsapp
    content = content.replace(/<a href="https:\/\/wa\.me.*?class="contact-menu-link">.*?<\/a>/gs, '');
    // Any other wa.me links - replace the whole a tag if possible, or just the href to tel
    content = content.replace(/href="https:\/\/wa\.me\/.*?"/g, 'href="tel:0553770127"');
    content = content.replace(/btn-whatsapp/g, 'btn-primary');
    content = content.replace(/fab fa-whatsapp/g, 'fas fa-phone');

    // 4. Remove social links in json-ld or footer
    content = content.replace(/"sameAs":\s*\[\s*".*?",\s*".*?",\s*".*?"\s*\]/g, '"sameAs": []');
    
    // 5. Add Location and keywords, we can append it to descriptions or titles.
    content = content.replace(/في مصر/g, 'في السعودية الرياض');
    content = content.replace(/مصر/g, 'السعودية الرياض');
    
    // Add specializations to the meta description or some hero desc
    const spec = 'متخصص في قص الخرسانه و قص الابواب ودرايش وتكسيرات وتكسير بلاط جميع التكسير وفتحات كور من 1 بوصة ل 16 بوصة والقص بمنشار ليزر في السعودية الرياض';
    content = content.replace(/<meta name="description"\s*content="(.*?)"/g, `<meta name="description" content="$1 ${spec}">`);

    // In the hero description
    content = content.replace(/شريكك الموثوق لتنفيذ كافة أعمال/g, `شريكك الموثوق في السعودية الرياض لتنفيذ كافة أعمال ${spec}، `);

    // Some SEO repetitions in the footer
    content = content.replace(/جميع الحقوق محفوظة لـ/g, 'السعودية الرياض - السعودية الرياض - جميع الحقوق محفوظة لـ');

    fs.writeFileSync(path.join(dir, file), content, 'utf8');
});

// Fix CSS colors
if (fs.existsSync(cssFile)) {
    let cssContent = fs.readFileSync(cssFile, 'utf8');
    
    // Convert primary/secondary/accent to black/white/gray
    cssContent = cssContent.replace(/--primary:\s*#[0-9a-fA-F]+;/g, '--primary: #000000;');
    cssContent = cssContent.replace(/--secondary:\s*#[0-9a-fA-F]+;/g, '--secondary: #333333;');
    cssContent = cssContent.replace(/--accent:\s*#[0-9a-fA-F]+;/g, '--accent: #666666;');
    cssContent = cssContent.replace(/--whatsapp:\s*#[0-9a-fA-F]+;/g, '--whatsapp: #000000;');
    
    // In case they are defined differently
    cssContent = cssContent.replace(/#ff6a00/gi, '#000000'); // Assuming orange was used
    cssContent = cssContent.replace(/#17191c/gi, '#ffffff'); // BG dark to white
    cssContent = cssContent.replace(/#212429/gi, '#f5f5f5'); // BG card to light gray
    cssContent = cssContent.replace(/--bg-dark:\s*#17191c;/g, '--bg-dark: #ffffff;');
    cssContent = cssContent.replace(/--bg-card:\s*#212429;/g, '--bg-card: #f5f5f5;');
    cssContent = cssContent.replace(/--text-main:\s*#a0a5aa;/g, '--text-main: #333333;');
    
    fs.writeFileSync(cssFile, cssContent, 'utf8');
}

console.log('Done modifying files.');
