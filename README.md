# Flask Movie Downloader with qBittorrent Integration

This is a Python Flask application that allows users to search for movies and automate the download of torrents using qBittorrent's Web API. The app provides a simple web interface where users can search for movies, and with a single click, start downloading selected torrents through qBittorrent.

## Features
- **Search movies** from a specified API.
- **Download torrents** directly to qBittorrent using magnet links.
- **Magnet link generation** with multiple torrent trackers included.
- **Basic HTTP Authentication** for secure communication with the qBittorrent Web API.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- **Python 3.x** installed on your machine.
- **Flask** and **requests** Python libraries installed.
- A **qBittorrent** instance running with the Web UI enabled.

You can install Flask and requests using pip:
```bash
pip install flask requests
```

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```
2. Navigate into the project directory:
    ```bash
    cd your-repo-name
    ```
3. Replace the placeholders in the code with your actual qBittorrent credentials:
    ```python
    QBITTORRENT_USERNAME = "QBUSER"
    QBITTORRENT_PASSWORD = "QPASS"
    ```
4. Replace the `QBITTORRENT_URL` in the code with your local or remote qBittorrent Web UI URL (default is `http://localhost:8080`).

## Running the App
To run the application, execute the following command in your terminal:
```bash
python app.py
```
This will start the Flask development server on `http://0.0.0.0:5000`. 

## Usage
### 1. Search for Movies
- Open your browser and go to `http://localhost:5000`.
- Use the search bar to look for movies using keywords, which sends a request to the specified API to fetch matching results.

### 2. Download a Movie
- Once the search results appear, select a movie and start the download.
- The app will generate a magnet link for the torrent and send it to your qBittorrent instance to begin downloading.

## API Endpoints
The application provides the following endpoints:
- **GET `/search`**: Accepts a query parameter (`?query`) and searches for movies via the specified API.
- **POST `/download`**: Starts the download by accepting the torrent's hash and movie name in the request body and sending the magnet link to qBittorrent.

## Magnet Link Construction
Magnet links are generated using the torrent hash and movie name, along with several predefined torrent trackers to ensure the availability of peers.

## Configuration
- Modify the qBittorrent URL and credentials (`QBITTORRENT_URL`, `QBITTORRENT_USERNAME`, `QBITTORRENT_PASSWORD`) to match your qBittorrent Web UI setup.

## Error Handling
The app returns JSON error responses in cases of:
- Missing parameters for the download request.
- Failed requests to the specified API or qBittorrent API.
- Network or authentication issues.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
