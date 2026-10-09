# -*- coding: utf-8 -*-
import urllib.request
import re
import json

url = "https://www.youtube.com/watch?v=Mi2kHwmy9Jk"
req = urllib.request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
    }
)
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8", errors="ignore")

    # Save html snippet
    with open("youtube_page.html", "w", encoding="utf-8") as out:
        out.write(html)

    # Title
    m_title = re.search(r"<title>(.*?)</title>", html)
    print("Title:", m_title.group(1) if m_title else "Not found")

    # ytInitialPlayerResponse
    m_player = re.search(r"ytInitialPlayerResponse\s*=\s*(\{.*?\});", html)
    if m_player:
        player_data = json.loads(m_player.group(1))
        video_details = player_data.get("videoDetails", {})
        print("Video Title:", video_details.get("title"))
        print("Author:", video_details.get("author"))
        print("Short Description:\n", video_details.get("shortDescription")[:1000])

        # captions
        captions = player_data.get("captions", {}).get("playerCaptionsTracklistRenderer", {}).get("captionTracks", [])
        print("Captions found:", len(captions))
        for c in captions:
            print("Language:", c.get("name", {}).get("simpleText"), "BaseUrl:", c.get("baseUrl")[:100])
            # download first caption
            cap_req = urllib.request.Request(c.get("baseUrl"), headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(cap_req) as c_resp:
                cap_xml = c_resp.read().decode("utf-8", errors="ignore")
                with open("transcript.xml", "w", encoding="utf-8") as c_out:
                    c_out.write(cap_xml)
                print("Saved transcript.xml (size: %d)" % len(cap_xml))
            break
    else:
        print("ytInitialPlayerResponse not found")
except Exception as e:
    print("Error:", e)
