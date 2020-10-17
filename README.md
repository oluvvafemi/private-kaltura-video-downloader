# kaltura video downloader

Based on this[ UBC kaltura video downloader](https://github.com/DonneyF/ubc-kaltura-video-downloader).

Download private kaltura videos that you have access to. The script should also work for public access videos.

To get the video download source, play the video and check the GET request. The link may be of the form : "https://cfvod.kaltura.com/scf/hls/p/...."

*If using conda:* `conda env create -f environment.yml` 

**To run:**  `python3 fetch_videos.py -src <"url ending in .mp4"> -qstr <"query string"> -output <output filename>`
