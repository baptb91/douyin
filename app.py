from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# Exemple : mots-clés chinois par niche
NICHES = {
    "cuisine": ["美食", "厨房", "烹饪"]
}

@app.route("/scrape", methods=["GET"])
def scrape():
    niche = request.args.get("niche", "cuisine")
    keywords = NICHES.get(niche, [])

    results = []
    for kw in keywords:
        # Simule un scraping (à remplacer par vrai scraper Douyin)
        response = requests.get(f"https://douyin-api-proxy.com/search?kw={kw}")
        for item in response.json().get("videos", []):
            upload_time = datetime.fromtimestamp(item["upload_time"])
            if upload_time > datetime.now() - timedelta(hours=24):
                results.append({
                    "title": item["title"],
                    "likes": item["likes"],
                    "upload_time": upload_time.isoformat(),
                    "video_url": item["video_url"],
                    "thumbnail_url": item["thumbnail"]
                })

    return jsonify(results)
