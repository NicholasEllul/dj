import subprocess
import os
from audio.base_downloader import BaseDownloader
from audio.platform import Platforms

class SoundCloudDownloader(BaseDownloader):
    def __init__(self, output_dir):
        super().__init__(output_dir, Platforms.SOUNDCLOUD)

    def search_and_download(self, search_term):
        command = [
            'yt-dlp',
            '-S', 'acodec:mp3',
            '-o', os.path.join(self.output_dir, '%(title)s.%(ext)s'),
            '--no-overwrites',
            f'scsearch:{search_term}'
        ]

        return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
