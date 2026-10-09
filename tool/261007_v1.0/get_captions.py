# -*- coding: utf-8 -*-
import json
import re
import urllib.request
import xml.etree.ElementTree as ET

with open("youtube_page.html", "r", encoding="utf-8") as f:
    html = f.read()

m_player = re.search(r"ytInitialPlayerResponse\s*=\s*(\{.*?\});", html)
if m_player:
    player_data = json.loads(m_player.group(1))
    video_details = player_data.get("videoDetails", {})
    print("=== VIDEO DETAILS ===")
    print("Title:", video_details.get("title"))
    print("Author:", video_details.get("author"))
    print("ViewCount:", video_details.get("viewCount"))
    print("Description:\n", video_details.get("shortDescription"))
    
    captions = player_data.get("captions", {}).get("playerCaptionsTracklistRenderer", {}).get("captionTracks", [])
    if captions:
        base_url = captions[0].get("baseUrl")
        print("\nCaption Base URL:", base_url)
        # try fetching with &fmt=json3
        for fmt in ["", "&fmt=json3", "&fmt=srv3"]:
            try:
                test_url = base_url + fmt
                req = urllib.request.Request(test_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                with urllib.request.urlopen(req) as r:
                    content = r.read().decode("utf-8", errors="ignore")
                    print(f"Fmt '{fmt}' fetched length: {len(content)}")
                    if len(content) > 0:
                        with open("captions_data.txt", "w", encoding="utf-8") as out:
                            out.write(content)
                        break
            except Exception as e:
                print(f"Fmt '{fmt}' error: {e}")
