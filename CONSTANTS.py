#!/usr/bin/python3

import pathlib

# USERNAME AND PASSWORD
USERNAME = ""
PASSWORD = ""

# TO GET THE EPISODE JSON INFORMATION
HEADERS = {
    'x-api-key': '857a1e5d-e35e-4fdf-805b-a87b6f8364bf',
    'Realm': 'dce.wwe',
    'x-app-var': '6.0.1.f8add0e'
}

# FOR THE DOWNLOADER
DOWNLOAD_HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'}
BASE_DIR = pathlib.Path(__file__).parent.resolve()
OUTPUT_FOLDER = f"{BASE_DIR}/output"
TEMP_FOLDER = f"{BASE_DIR}/temp"

# DATABASE
DB_FILE = f"{BASE_DIR}/events.db"

# VIDEO SIZE INFORMATION
VIDEO_QUALITY = [8000, # 1080p high
                 5000,  # 1080p low
                 4000,  # 720p high
                 2000,  # 720p low
                 1500,  # 504p
                 1000,  # 360p
                 600]   # 288p

if __name__ == "__main__":
    print("Please run python main.py instead.")
    pass
