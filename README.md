## WWE Network 2.0.1 Downloader (Improved further)

### Edits made by Homer3k

- Fixed some errors (?) in latest source code
    - Maybe not all or none of these "errors" are really errors. It's always possible I just didn't get what was intended.
- Added __-l/--language__ flag for downloading different audio languages
- Added Shell-script for easier usage

#### Instructions

Follow the [Prerequisites](#prerequisites) first.

###### Make Shell-script executable:
```
sudo chmod +x /path/to/project/wwe-dl.sh
```
###### Create symlink to use it from everywhere on your system:
```
sudo ln -s /path/to/project/wwe-dl.sh /usr/local/bin/wwedl
```
###### Call the script to download a video from WWE Network:
```
// downloading english audio by default
wwedl https://network.wwe.com/video/xxxxx

// downloading a different language (e.g. german)
wwedl https://network.wwe.com/video/xxxxx deu
```

The video file is downloaded to the directory from within the script is executed. Temp files and SQLite-database will be placed in project-directory. If the selected language is not found it will download english as default.

By default the script forces the video to download (-f) and adds milestone chapters (-c). It also adds a default start (-st) and endtime (-et) to always download the whole video. You can change this behavior by editing `wwe-dl.sh` in the projects root according to your personal needs. You can find the [Options](#options) for the script further down this file.

###### Credit

Full credit for the original Python script goes to [freyta](https://github.com/freyta) with his version of the
[WWE-Network-Downloader](https://github.com/freyta/WWE-Network-Downloader). Thank you for the great work you have done there!

### Original Documentation (edited)

Freyta's WWE Network 2.0 Downloader using Python3. This was coded by me from scratch, ideas were taken from youtube-dl.

Features include the following:
- Downloading from set start times
- Ending at certain times (i.e. only downloading certain matches)
- Qualtiy selection (1 being 1080p, 6 being 288p)
- Kodi NFO file creations (TV episode and Series only at the moment - PPV needs to be added)
- Part downloading of files.

### Prerequisites

You must have at least version 4.2 ffmpeg installed and in your PATH. You also need Python3 installed on your system.

#### 1. Using pip3 install the required modules:

```
pip3 install --user -r requirements.txt
```

You may need to break the system packages if you encounter an error. Do at you own risk!

```
pip3 install --user -r requirements.txt --break-system-packages
```

#### 2. Edit the username and password variables in CONSTANTS.py to include your subscription email and password

```
...
# USERNAME AND PASSWORD
USERNAME = "YOUR_EMAIL_ADDRESS"
PASSWORD = "YOUR_PASSWORD"
...
```

### Usage instructions

Follow the [Instructions](#instructions) from here on if you want to use the Shell-script.

###### Basic video download:

```
python3 main.py -t https://watch.wwe.com/episode/SmackDown-130268
```

###### Download with start and end times, using custom file name:

```
python3 main.py -st 1619.934 -et 1712.834 -of 'Tucker confronts Mandy Rose Smackdown 02-21-2020' -t https://watch.wwe.com/episode/SmackDown-130268
```

###### Download chapterised 720p video with Kodi series and episode NFO files:

```
python3 main.py -c -q 3 -s -e -t https://watch.wwe.com/episode/Bret-Hart-132278
```

### Options

> **-t/--title** - Link to the video you want to download.\
> **-q/--quality** - Quality of the video you want to download. 1 is 1080p high (default) 6 being 288p (lowest).\
> **-c/--chapter** - Add milestone chapters to the video.\
> **-s/--subtitles** - Downloads the subtitles.\
> **-k/--keep_files** - Keep temporary aac and ts files.\
> <strike>**-e** - Write a Kodi episode NFO file.</strike> *\
> <strike>**-s** - Write a Kodi series NFO file with poster and fanart.</strike> *\
> **-st/--start_time** - Start time in seconds from where you want to start downloading.\
> **-et/--end_time** - End time in seconds from where you want to finish downloading.\
> **-f/--force** - Force the download of the video. Overwrites previously downloaded files.\
> **-of/--output_filename** - Specify a custom filename for the output.\
> **-l/--language** - Audio language of the video. Defaults to "eng" (english).

\* Hint by Homer3k: There is no handling for these options in the source code so I guess this was not implemented yet.