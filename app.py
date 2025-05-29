from flask import Flask, request, jsonify
import os
from datetime import datetime, timedelta

app = Flask(__name__)

# Simulation de vidéos pour test (à remplacer par un vrai scraper)
SIMULATED_VIDEOS = {
    "美食": [
        {
            "title": "Recette incroyable de nouilles",
            "likes": 15400,
            "upload_time": datetime.now().timestamp(),  # aujourd'hui
            "video_url": "https://example.com/video1.mp4",
            "thumbnail_url": "https://example.com/thumb1.jpg"
        },
        {
            "title": "Gâteau en 5 minutes",
            "likes": 9800,
            "upload_time": (datetime.now() - timedelta(hours=2)).timestamp(),
            "video_url": "https://example.com/video2.mp4",
            "thumbnail_url": "https://example.com/thumb2.jpg"
        }
    ]
}

# Mots-clés chinois par niche
NICHES = {
    "cuisine": ["美食"]
}

@app.route("/scrape", methods=["GET"])
def scrape():
    niche = request.args.get("niche", "cuisine")
    keywords = NICHES.get(niche, [])
    
    results = []
    for kw in keywords:
        videos = SIMULATED_VIDEOS.get(kw, [])
        for video in videos:
            upload_time = datetime.fromtimestamp(video["upload_time"])
            if upload_time > datetime.now() - timedelta(hours=24):
                results.append({
                    "title": video["title"],
                    "likes": video["likes"],
                    "upload_time": upload_time.isoformat(),
                    "video_url": video["video_url"],
                    "thumbnail_url": video["thumbnail_url"]
                })

    return jsonify(results)

# OBLIGATOIRE POUR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
