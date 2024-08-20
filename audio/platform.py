from enum import Enum

class Platforms(Enum):
    SOUNDCLOUD = "soundcloud"
    YOUTUBE = "youtube"

class Platform:
    def __init__(self, *, name, abbreviation, downloader):
        self.name = name
        self.abbreviation = abbreviation
        self.downloader = downloader

    def abbreviation(self):
        return self.abbreviation
    
    def name(self):
        return self.name
    
    def downloader(self):
        return self.downloader
