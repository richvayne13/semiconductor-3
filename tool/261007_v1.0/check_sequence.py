import re

for p in ['result/261007_v1.0/index.html', 'index.html']:
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()

    navs = re.findall(r'<li class="nav-item"><a href="#q-(\d+)"[^>]*><span class="nav-num">(\d+)</span><span class="nav-text">(.*?)</span>', text)
    secs = re.findall(r'<section class="[^"]*" id="q-(\d+)">.*?<span class="topic-badge">Q (\d+)</span>.*?<h2 class="topic-title">(.*?)</h2>', text, re.DOTALL)
    nav_nums = [int(n[0]) for n in navs]
    sec_nums = [int(s[0]) for s in secs]
    print(f"{p}: navs_count={len(navs)}, secs_count={len(secs)}, navs_1_95={nav_nums == list(range(1, 96))}, secs_1_95={sec_nums == list(range(1, 96))}")
