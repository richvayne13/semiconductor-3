import re

for path in ['result/261007_v1.0/index.html', 'index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    navs = len(re.findall(r'<li class="nav-item">', content))
    secs = len(re.findall(r'<section class="[^"]*topic-section', content))
    q01 = 'id="q-01"' in content
    q89 = 'id="q-89"' in content
    print(f"{path}: navs={navs}, secs={secs}, q01={q01}, q89={q89}")
