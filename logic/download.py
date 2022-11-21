from pytube import YouTube, Playlist, Search
from shutil import make_archive, move
import os
from glob import glob


class AudioDownloader:

    def __init__(self, find=None, playlist=None, link=None):
        print(" | ", find, " | ", playlist, " | ", link, " | ")
        self.clear_temp()

    def clear_temp(self):
        for file in glob('temp/*'):
            os.remove(file)

    def playlist_download(self, playlist):
        playlist = Playlist(playlist)

        for video in playlist.videos:
            try:
                out_file = video.streams.get_audio_only().download('temp/')
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                print(new_file)
            except AttributeError:
                return False, 'Error'

        file_name = "songs"
        directory = "temp"
        file_zip = make_archive(file_name, "zip", directory)
        move(file_zip, directory)

    def link_download(self, link):
        yt = YouTube(link)
        streams = yt.streams.get_audio_only()
        return self.to_mp3(streams)

    def search_download(self, text):
        search = Search(text)
        yt = YouTube('https://www.youtube.com/watch?v=' +
                     getattr(search.results[0], 'video_id'))
        streams = yt.streams.get_audio_only()
        return self.to_mp3(streams)

    def to_mp3(self, streams):
        try:
            out_file = streams.download('temp/')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(new_file)
            return new_file
        except AttributeError:
            return False


if __name__ == '__main__':
    print('iniciado')
    aD = AudioDownloader()
    print(aD.search_download('lil peep'))
    print(aD.link_download(
        'https://www.youtube.com/watch?v=34_rvjuwxPk&ab_channel=Axceels'))
    print(aD.playlist_download(
        'https://www.youtube.com/playlist?list=PLIreEdTT6HJfR0bXGCc2_Ax8Wq2hL8Mbp'))
