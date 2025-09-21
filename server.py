from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Zenék JSON – csak a fájlnevek
tracks = [
    {"title": "Song 1", "file": "song1.mp3", "cover": "cover1.png"},
    {"title": "Song 2", "file": "song2.mp3", "cover": "cover2.png"},
]

@app.route('/tracks')
def get_tracks():
    return jsonify(tracks)

@app.route('/musics/<path:filename>')
def serve_music(filename):
    return send_from_directory('.', filename)  # gyökérkönyvtárból szolgálja ki

@app.route('/covers/<path:filename>')
def serve_cover(filename):
    return send_from_directory('.', filename)  # gyökérkönyvtárból szolgálja ki

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
