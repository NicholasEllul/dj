import subprocess
import os
from audio.platform import Platforms
from audio.base_downloader import BaseDownloader

class YouTubeDownloader(BaseDownloader):
    def __init__(self, output_dir):
        super().__init__(output_dir, Platforms.YOUTUBE)

    def search_and_download(self, search_term):
        command = [
            'yt-dlp',
            '--extract-audio',
            '--audio-format', "mp3",
            '-o', os.path.join(self.output_dir, '%(title)s.%(ext)s'),
            '--no-overwrites',
            f'ytsearch:{search_term}'
        ]

        return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)