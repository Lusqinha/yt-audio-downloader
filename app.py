from flask import Flask, render_template, send_file, request
from logic.download import AudioDownloader

aD = AudioDownloader()

app = Flask(__name__)


def alert(message):
    return render_template('alert.html', message=message)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download', methods=['GET', 'POST'])
def download():
    url = request.form['pesquisa']
    if url.startswith('https://www.youtube.com/playlist?'):
        aD.playlist_download(url)
        return send_file('temp/songs.zip', as_attachment=True)
    elif url.startswith('https://www.youtube.com/watch?'):
        arquivo = aD.link_download(url)
        return send_file(arquivo, as_attachment=True)
    elif url == "":
        return False
    else:
        arquivo = aD.search_download(url)
        return send_file(arquivo, as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)
