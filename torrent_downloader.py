import requests
from flask import Flask, render_template, request, jsonify
from requests.auth import HTTPBasicAuth
import urllib.parse

app = Flask(__name__)

# Replace with your qBittorrent API URL
QBITTORRENT_URL = "http://localhost:8080/api/v2/torrents/add"

# Replace these with your actual credentials
QBITTORRENT_USERNAME = "YOUR_QBITTORRENT_USERNAME"
QBITTORRENT_PASSWORD = "YOUR_QBITTORRENT_PASSWORD"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    # Replace the API URL with your movie search API endpoint
    response = requests.get("YOUR_MOVIE_API_URL", params={'query_term': query})
    return jsonify(response.json())

@app.route('/download', methods=['POST'])
def download():
    torrent_hash = request.json.get('torrent_hash')
    movie_name = request.json.get('movie_name')
    if not torrent_hash or not movie_name:
        return jsonify({"error": "Missing torrent hash or movie name"}), 400

    magnet_link = construct_magnet_link(torrent_hash, movie_name)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {'urls': magnet_link}
    
    try:
        response = requests.post(
            QBITTORRENT_URL,
            headers=headers,
            data=payload,
            auth=HTTPBasicAuth(QBITTORRENT_USERNAME, QBITTORRENT_PASSWORD)
        )
        
        if response.status_code == 200:
            return jsonify({"message": "Download started successfully"}), 200
        else:
            return jsonify({"error": f"Failed to start download: {response.status_code} - {response.text}"}), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": f"Request failed: {e}"}), 500

def construct_magnet_link(torrent_hash, movie_name):
    base_url = "magnet:?xt=urn:btih:"
    encoded_name = urllib.parse.quote_plus(movie_name)
    trackers = [
        "udp://open.demonii.com:1337/announce",
        "udp://tracker.openbittorrent.com:80",
        "udp://tracker.coppersurfer.tk:6969",
        "udp://glotorrents.pw:6969/announce",
        "udp://tracker.opentrackr.org:1337/announce",
        "udp://torrent.gresille.org:80/announce",
        "udp://p4p.arenabg.com:1337",
        "udp://tracker.leechers-paradise.org:6969"
    ]
    magnet_link = f"{base_url}{torrent_hash}&dn={encoded_name}"
    for tracker in trackers:
        magnet_link += f"&tr={urllib.parse.quote(tracker)}"
    return magnet_link

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)