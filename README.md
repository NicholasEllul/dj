# DJ
A wrapper around yt-dlp to quickly download songs for mixing at home.

## Setup

Before starting ensure you have the following installed:
* [yt-dlp](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#installation)
* Python 3.8+

## Configuration

**Configuring default output directory**
* To avoid having to specify the output directory each time you download a track, you can set the `DJ_DEFAULT_AUDIO_OUTPUT_DIR` environment variable for your shell.

**Using this tool from anywhere in your terminal**
* To call this tool from any directory in your terminal, you should add this repository's path to your PATH environment variable. Instructions on how to do so vary between MacOS/Linux & Windows.

## Usage
> SoundCloud and YouTube are supported

### SoundCloud

**Search and download a track**

```sh
dj sc -s "Search term here" -o "path/to/output/dir"
```

**Download a track by URL**

```sh
dj sc -u "https://soundcloud.com/example/example" -o "path/to/output/dir"
```

### YouTube 

**Search and download a track**

```sh
dj yt -s "Search term here" -o "path/to/output/dir"
```

**Download a track by URL**

```sh
dj yt -u "https://www.youtube.com/watch?v=abcdefgh" -o "path/to/output/dir"
```
