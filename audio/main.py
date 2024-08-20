#!/usr/bin/env python3

import os, argparse, shutil
from audio.soundcloud_downloader import SoundCloudDownloader
from audio.youtube_downloader import YouTubeDownloader
from audio.platform import Platforms, Platform

SUPPORTED_PLATFORMS = [
    Platform(
        name=Platforms.SOUNDCLOUD,
        abbreviation="sc",
        downloader=SoundCloudDownloader
    ),
    Platform(
        name=Platforms.YOUTUBE,
        abbreviation="yt",
        downloader=YouTubeDownloader
    )
]

def main():
    parser = configure_cmd_args()
    args = parser.parse_args()

    validate_dependencies_and_inputs(args)

    selected_platform = next((platform for platform in SUPPORTED_PLATFORMS if platform.abbreviation == args.platform), None)

    audio_downloader = selected_platform.downloader(args.output_dir)
    process = audio_downloader.download_from_url(args.url) if args.url else audio_downloader.search_and_download(args.search_term)

    stream_process_output(process)

    process.wait()

    if process.returncode == 0:
        print("Download completed successfully.")
    else:
        print("Download failed.")

    exit(0)

def configure_cmd_args():
    parser = argparse.ArgumentParser(description='Download a track from youtube or soundcloud.')
    
    platform_choices = [platform.abbreviation for platform in SUPPORTED_PLATFORMS]
    
    # Position arguments
    parser.add_argument('platform', choices=platform_choices,
                        help='Platform to download from (sc for SoundCloud or yt for YouTube).')
    
    # Flag arguments
    search_type_arg_group = parser.add_mutually_exclusive_group(required=True)
    search_type_arg_group.add_argument('-s', '--search-term', help='Name of the song to search and download.')
    search_type_arg_group.add_argument('-u', '--url', help='URL of the song to download directly.')
    
    environment_output_dir = os.getenv("DJ_DEFAULT_AUDIO_OUTPUT_DIR")
    parser.add_argument('-o', '--output-dir', default=environment_output_dir, required=False, 
                        help=f'Directory to save the file to. Overrides the DJ_DEFAULT_AUDIO_OUTPUT_DIR environment variable if set.')
    
    return parser


def validate_dependencies_and_inputs(args):
    # Validate a directory is specified
    if not args.output_dir:
        raise ValueError("Error: No output directory specified. Please specify an output directory using the -o flag, or set the DJ_DEFAULT_AUDIO_OUTPUT_DIR environment variable.")

    # Validate a directory is able to be written to
    path = os.path.expanduser(args.output_dir)
    if not os.path.isdir(path):
        raise ValueError(f"Error: The specified output directory '{path}' is not a valid directory.")
    
    # Validate yt-dlp installation
    if shutil.which('yt-dlp') is None:
        raise ValueError("Error: yt-dlp is not installed. Please install it and try again. "
            "(See https://github.com/yt-dlp/yt-dlp#installation)")


def stream_process_output(process):
    for line in process.stdout:
        print(line, end='')
    for line in process.stderr:
        print(line, end='')

if __name__ == '__main__':
    main()
