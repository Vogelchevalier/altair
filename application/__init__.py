import os
from flask import Flask, url_for

app = Flask(__name__)

from application import lastfm


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


@app.context_processor
def lastfmtrack():
    return dict(song=lastfm.getPlayingTrack())


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


from application import views
from application import uploader


if __name__ == "__main__":
    app.run(debug=True)
