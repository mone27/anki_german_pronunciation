import shutil
import requests
from bs4 import BeautifulSoup
from pathlib import Path


base_url = "https://dict.leo.org/italienisch-deutsch/"
audio_url = "https://dict.leo.org/media/audio/"
# this probably can be taken from anki
dest_folder = "/home/simone/.var/app/net.ankiweb.Anki/data/Anki2/Simone/collection.media/"



def get_page(word):
    r = requests.get(base_url + word)
    return BeautifulSoup(r.text, features="lxml")


def get_audio_id(page):
    audio_tag = page.select("#centerColumn > div > div:nth-child(2) tbody  tr:nth-child(1) td:nth-child(7) i")[0]
    return audio_tag.attrs['data-dz-rel-audio']

def download_audio(audio_id, word):
    url = audio_url + audio_id + ".ogg"

    path = Path(dest_folder) / (word + ".ogg")
    r = requests.get(url)
    with open(path, 'wb') as f:
         f.write(r.content)

    return path.name

def download_pronunciation(word):
    page = get_page(word)
    audio_id = get_audio_id(page)
    return download_audio(audio_id, word)

download_pronunciation("torre")