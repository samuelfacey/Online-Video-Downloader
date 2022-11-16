from __future__ import unicode_literals
from youtube_dl import YoutubeDL
from youtube_dl.utils import DownloadError
import traceback



def download(link,format):
    
    YDL_OPTS = {'format': 'bestaudio/best','noplaylist':'True', 'outtml': 'song.%(ext)s', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': format, 'preferredquality': '192' }],'default_search':'auto', 'nocheckcertificates':'true'}
    
    with YoutubeDL(YDL_OPTS) as ydl:
        ydl.download([link])

        