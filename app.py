from flask import Flask, render_template, send_file, request
from logic.download import Download

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download', methods=['GET', 'POST'])
def download():
    url = request.form['pesquisa']
    d = Download(url)
    return send_file(d.download(), as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
