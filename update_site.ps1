$dir = "c:\webs\السعودية يبويا"
$htmlFiles = Get-ChildItem -Path $dir -Filter "*.html"

$spec = "متخصص في قص الخرسانه و قص الابواب ودرايش وتكسيرات وتكسير بلاط جميع التكسير وفتحات كور من 1 بوصة ل 16 بوصة والقص بمنشار ليزر في السعودية الرياض"

foreach ($file in $htmlFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8

    # Names
    $content = $content -replace 'Expert-Core', 'ابو عبد الرحمن'
    $content = $content -replace 'إشراف المهندس / معتصم حمدي', 'ابو عبد الرحمن'
    $content = $content -replace 'المهندس معتصم حمدي', 'ابو عبد الرحمن'
    $content = $content -replace 'البشمهندس معتصم', 'ابو عبد الرحمن'
    $content = $content -replace 'معتصم حمدي', 'ابو عبد الرحمن'

    # Phones
    $content = $content -replace '010 3383 1671', '0553770127'
    $content = $content -replace '01033831671', '0553770127'
    $content = $content -replace '011 5280 0018', '0553770127'
    $content = $content -replace '01152800018', '0553770127'
    $content = $content -replace '\+201033831671', '+966553770127'
    $content = $content -replace '\+201152800018', '+966553770127'

    # Whatsapp
    $content = $content -replace '(?s)<a href="https://wa\.me.*?class="floating-whatsapp".*?</a>', ''
    $content = $content -replace '(?s)<a href="https://wa\.me.*?class="header-whatsapp".*?</a>', ''
    $content = $content -replace '(?s)<a href="https://wa\.me.*?class="contact-menu-link">.*?</a>', ''
    $content = $content -replace 'href="https://wa\.me/[^"]*"', 'href="tel:0553770127"'
    $content = $content -replace 'btn-whatsapp', 'btn-primary'
    $content = $content -replace 'fab fa-whatsapp', 'fas fa-phone'

    # Social links in Schema
    $content = $content -replace '"sameAs":\s*\[\s*".*?",\s*".*?",\s*".*?"\s*\]', '"sameAs": []'

    # Location
    $content = $content -replace 'في مصر', 'في السعودية الرياض'

    # Descriptions
    $content = [regex]::Replace($content, '(?i)<meta name="description"\s*content="(.*?)"', { param($m) '<meta name="description" content="{0} {1}"' -f $m.Groups[1].Value, $spec })

    # Hero description
    $content = $content -replace 'شريكك الموثوق لتنفيذ كافة أعمال', ("شريكك الموثوق في السعودية الرياض لتنفيذ كافة أعمال " + $spec + "، ")

    # Footer
    $content = $content -replace 'جميع الحقوق محفوظة لـ', 'السعودية الرياض - السعودية الرياض - جميع الحقوق محفوظة لـ'

    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
}

$cssFile = "$dir\style.css"
if (Test-Path $cssFile) {
    $cssContent = Get-Content -Path $cssFile -Raw -Encoding UTF8

    $cssContent = $cssContent -replace '--primary:\s*#[0-9a-fA-F]+;', '--primary: #000000;'
    $cssContent = $cssContent -replace '--secondary:\s*#[0-9a-fA-F]+;', '--secondary: #333333;'
    $cssContent = $cssContent -replace '--accent:\s*#[0-9a-fA-F]+;', '--accent: #666666;'
    $cssContent = $cssContent -replace '--whatsapp:\s*#[0-9a-fA-F]+;', '--whatsapp: #000000;'

    $cssContent = $cssContent -replace '(?i)#ff6a00', '#000000'
    $cssContent = $cssContent -replace '(?i)#17191c', '#ffffff'
    $cssContent = $cssContent -replace '(?i)#212429', '#f5f5f5'
    $cssContent = $cssContent -replace '--bg-dark:\s*#ffffff;', '--bg-dark: #ffffff;'
    $cssContent = $cssContent -replace '--bg-card:\s*#f5f5f5;', '--bg-card: #f5f5f5;'
    $cssContent = $cssContent -replace '--text-main:\s*#a0a5aa;', '--text-main: #333333;'

    Set-Content -Path $cssFile -Value $cssContent -Encoding UTF8
}
Write-Output "Done modifying files"
