import os
import secrets
from datetime import datetime
from flask import request, url_for
from PIL import Image
from application import app


@app.route("/test")
def test():
    return "testisivu"


@app.route("/upload", methods=["POST"])
def upload():

    f = open("/home/sami/secret.csv", "r")
    secret = f.readline()
    f.close()

    domain = "https://altair.fi"
    root_folder = "/home/sami/alter/i"

    if request.method == "POST":
        if request.form.to_dict(flat=False)['secret'][0] != secret:
            return "Unauthorized", 401
        else:
            month_folder = datetime.now().strftime("%Y-%m")
            day_time = datetime.now().strftime("%d_%H%M")

            file = request.files['image']
            extension = os.path.splitext(file.filename)[1]
            file.flush()

            image = Image.open(file)
            data = list(image.getdata())
            file_without_exif = Image.new(image.mode, image.size)
            file_without_exif.putdata(data)

            salt = secrets.token_urlsafe(5)
            filename = "".join([day_time, "-", salt, extension])

            if not os.path.exists(os.path.dirname(root_folder + "/" + month_folder)):
                os.makedirs(os.path.dirname(root_folder + "/" + month_folder))

            file_without_exif.save(os.path.join(root_folder + "/" + month_folder, filename))
            return "".join([domain, "/i/", month_folder, "/", filename]), 200
    else:
        return "Method not allowed", 405