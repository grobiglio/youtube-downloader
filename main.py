from typing import Tuple
from pytube import YouTube
from rich import print
from rich.table import Table
import clipboard
from clean_console import clean_console


def get_video_info(video_url: str) -> Tuple:
    try:
        yt = YouTube(video_url)
    except:
        return None, None

    video_title = yt.title
    video_streams = yt.streams

    options_table = Table(title=video_title)

    options_table.add_column("Option #")
    options_table.add_column("itag")
    options_table.add_column("Format")
    options_table.add_column("Resolution")
    options_table.add_column("Type")

    for opt_no, stream in enumerate(video_streams, start=1):
        options_table.add_row(str(opt_no),
                              str(stream.itag),
                              stream.mime_type,
                              stream.resolution,
                              stream.type)

    return video_title, options_table


def download_video(video_url: str, option_number: int) -> None:
    yt = YouTube(video_url)
    video_title = yt.title
    print(f'Downloading [red bold]{video_title}[/], please wait...')
    yt.streams[option_number-1].download("./downloads")

    
clean_console()

print('Whelcome to Youtube downloader.')
dl_other = 'Y'

while dl_other == 'Y':
    input('Copy the video URL and press Enter when ready.')
    video_url = clipboard.paste()
    video_title, options_table = get_video_info(video_url)

    if video_title != None:
        print(options_table)
        dl_option = int(input('Choose option to download: '))
        download_video(video_url, dl_option)
        print('Download complete.')
    else:
        print('URL not valid, please try again.')

    dl_other = input('Do you want to download another video? (Y/n): ').upper()
    clean_console()
