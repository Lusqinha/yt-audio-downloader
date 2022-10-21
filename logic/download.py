from pytube import YouTube
import os
import glob


class Download:
    def __init__(self, url):
        self.url = url
        self.yt = YouTube(url)
        self.stream = self.yt.streams.filter(
            only_audio=True, file_extension="mp3").first()

    def download(self):
        self.stream.download('/temp')
        return self.stream.default_filename

    def get_title(self):
        return self.yt.title

    def get_author(self):
        return self.yt.author

    def del_video(self):
        os.remove('/temp/' + self.stream.default_filename + 'mp3')
        return True
