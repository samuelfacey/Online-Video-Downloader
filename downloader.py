from __future__ import unicode_literals
from youtube_dl import YoutubeDL
from youtube_dl.utils import DownloadError
import traceback
import os
import shutil


def download(link,format):
    
    YDL_OPTS = {'audioformat':format, 'format': 'bestaudio/best','noplaylist':'True', 'outtml':'/static/storage/song', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192' }],'default_search':'auto', 'nocheckcertificates':'true'}
    
    with YoutubeDL(YDL_OPTS) as ydl:
        i = ydl.extract_info(link,download=False)
        info = {
            'title': i['title'],
            'format': format
        }
        try:
            os.remove(f"static\storage\{info['title']}.{info['format']}")
        except:
            pass
        ydl.download([link])
        info['name'] = f"{info['title']}.{info['format']}"
        for file in os.listdir():
            if file.endswith(f'.{format}'):
                os.rename(file, info['name'])
                shutil.move(info['name'], f'static\storage\{info["name"]}')
    
    return info

        