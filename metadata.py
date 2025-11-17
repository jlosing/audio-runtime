import mutagen
from mutagen.flac import FLAC
import os
import argparse

parser = argparse.ArgumentParser(description="A small program that calculates total runtime of audio files")
parser.add_argument("directory", type=str, help="the directory you want to be recursivly searched")

args = parser.parse_args()

if args.directory is None:
    raise TypeError("no directory provided")
directoryToSearch = args.directory
    

def find_audio_files(directory):
    found_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            _base, extension = os.path.splitext(file)
            if "flac" in extension.lower():
                found_files.append(os.path.join(root, file))
    return found_files

def get_runtimes(files):
    runtime = 0
    for file in files:
        audio = FLAC(file)
        runtime += audio.info.length
    return runtime

files = find_audio_files(directoryToSearch)
runtime = get_runtimes(files)
print("Total Runtime: ", runtime, " seconds, ")
print(runtime/60, "minutes")


