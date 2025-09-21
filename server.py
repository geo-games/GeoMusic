from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Mappa a zenéknek és borítóknak
MUSIC_DIR = 'musics'
COVER_DIR = 'covers'

# Zenék JSON
tracks = [
    {"title": "Song 1", "file": "song1.mp3", "cover": "cover1.jpg"},
    {"title": "Song 2", "file": "song2.mp3", "cover": "cover2.jpg"},
    {"title": "Song 3", "file": "song3.mp3", "cover": "cover3.jpg"}
]

@app.route('/tracks')
def get_tracks():
    return jsonify(tracks)

@app.route('/musics/<path:filename>')
def serve_music(filename):
    return send_from_directory(MUSIC_DIR, filename)

@app.route('/covers/<path:filename>')
def serve_cover(filename):
    return send_from_directory(COVER_DIR, filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
