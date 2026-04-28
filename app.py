from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route('/api/extract', methods=['GET'])
def extract():
    video_url = request.args.get('url')
    
    if not video_url:
        return jsonify({"error": "URL parameter missing hai"}), 400

    ydl_opts = {
        'format': 'best', 
        'quiet': True,    
        'noplaylist': True 
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False) 
            
            return jsonify({
                "success": True,
                "title": info.get('title'),
                "thumbnail": info.get('thumbnail'),
                "duration": info.get('duration'),
                "direct_url": info.get('url') 
            })
            
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run()
