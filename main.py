import sys

from mutagen.mp3 import MP3

def main(path):
  audio = MP3(path)
  print('%.0fsms' % (audio.info.length * 1000))

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('usage: main.py <path to mp3>')
    sys.exit(1)
  main(sys.argv[1])