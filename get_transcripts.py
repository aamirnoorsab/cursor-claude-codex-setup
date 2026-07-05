from youtube_transcript_api import YouTubeTranscriptApi
import os

OUT_DIR = os.path.join("research", "youtube-transcripts")
os.makedirs(OUT_DIR, exist_ok=True)

videos = {
    "kevinindig_beyond_the_serp_trust_stack": "jxXPpXL2pFg",
    "lilyray_geo_aeo_llmo_mozcon": "2nJkT8zOzcM",
    "mariehaynes_google_ai_agent_seo": "gDt1vMsw3_Q",
    "wilreynolds_wrong_ai_metric_business_impact": "YVaRBvNXg6o",
    "randfishkin_ai_overviews_content_future": "5JQvdLYvGZI",
}

api = YouTubeTranscriptApi()

for label, video_id in videos.items():
    try:
        fetched = api.fetch(video_id, languages=["en"])
        text = " ".join(snippet.text for snippet in fetched.snippets)
        path = os.path.join(OUT_DIR, f"{label}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"OK: {label} ({len(text)} chars) -> {path}")
    except Exception as e:
        print(f"FAILED: {label} ({video_id}) -> {e}")