import re

for path in ['result/261007_v1.0/index.html', 'index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    navs = len(re.findall(r'<li class="nav-item">', content))
    secs = len(re.findall(r'<section class="[^"]*topic-section', content))
    q01 = 'id="q-01"' in content
    q90 = 'id="q-90"' in content
    print(f"{path}: navs={navs}, secs={secs}, q01={q01}, q90={q90}")
