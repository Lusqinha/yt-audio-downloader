from pytube import YouTube
from pytube import Search
import os
from glob import glob


class Download:
    def __init__(self, find=None):
        self.text = find
        self.search = Search(self.text)
        self.yt = YouTube('https://www.youtube.com/watch?v=' +
                          getattr(self.search.results[0], 'video_id'))
        self.streams = self.yt.streams.get_audio_only()
        for file in glob('temp/*'):
            os.remove(file)

    def get_title(self):
        return self.yt.title

    def download(self):
        try:
            out_file = self.streams.download('temp/')

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(new_file)
            return new_file
        except AttributeError:
            return False


if __name__ == '__main__':
    d = Download(find=input('Enter search: '))
    d.download()
