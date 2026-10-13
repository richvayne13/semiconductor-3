# -*- coding: utf-8 -*-
import re

for path in ['result/261007_v1.0/index.html', 'index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    navs = [int(x) for x in re.findall(r'href="#q-(\d+)"', content)]
    secs = [int(x) for x in re.findall(r'<section [^>]*id="q-(\d+)"', content)]
    expected = list(range(1, 105))
    print(f"Path: {path}")
    print(f"  Navs: len={len(navs)}, min={min(navs)}, max={max(navs)}, matches={navs == expected}")
    print(f"  Secs: len={len(secs)}, min={min(secs)}, max={max(secs)}, matches={secs == expected}")
