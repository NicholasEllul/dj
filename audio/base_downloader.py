import subprocess, os

class BaseDownloader:
    def __init__(self, output_dir, platform):
            self.output_dir = output_dir
            self.platform = platform

    def search_and_download(self, search_term):
        raise NotImplementedError("This method should be overridden.")

    def download_from_url(self, url):
        command = [
            'yt-dlp',
            '-S', 'acodec:mp3', 
            '-x', '--audio-format', 'mp3',
            '-o', os.path.join(self.output_dir, '%(title)s.%(ext)s'),
            '--no-overwrites',
            '--use-extractors', self.platform.value,
            url
        ]
        print(command)
        return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)