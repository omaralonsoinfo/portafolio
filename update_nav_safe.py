import os
import glob

html_files = glob.glob('*.html')
c = 0

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        old_nav = '<li><a href="proyectos.html">Proyectos</a></li>'
        new_nav = '<li><a href="proyectos.html">Proyectos</a></li>\n\t\t\t<li><a href="halloffame.html">Hall of Fame</a></li>'
        
        if old_nav in content and new_nav not in content:
            new_content = content.replace(old_nav, new_nav)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
            c += 1
    except Exception as e:
        print(f"Error processing {file}: {e}")
            
print(f"Total updated: {c}")
