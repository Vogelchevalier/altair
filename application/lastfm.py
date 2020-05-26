import requests
import xml.etree.ElementTree as elemTree


def getPlayingTrack():
    api_url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&limit=1"

    with open("/home/sami/last_fm_api_key.csv", "r") as f:
        username, key = f.readline().split(",")

    request_url = api_url + "&user=" + username + "&api_key=" + key

    response = requests.get(request_url)
    root = elemTree.fromstring(response.content)

    now_playing = root[0][0].get("nowplaying") == "true"

    artist = root[0][0][0].text
    song_title = root[0][0][1].text

    return artist + " - " + song_title if now_playing else "Nothing"

