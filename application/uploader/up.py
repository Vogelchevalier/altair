# Inspiration from:
# https://github.com/markylon/flask-sharex
# Under GPLv3. See LICENSE in application/uploader

import os
import secrets
from datetime import datetime
from flask import request
from PIL import Image
from application import app


@app.route("/upload", methods=["POST"])
def upload():

    with open("/home/sami/secret.csv", "r") as f:
        secret = f.readline()

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

            if not os.path.exists(root_folder + "/" + month_folder):
                os.makedirs("".join([root_folder, "/", month_folder]), exist_ok=True)

            file_without_exif.save(os.path.join(root_folder + "/" + month_folder, filename))
            return "".join([domain, "/i/", month_folder, "/", filename]), 200
    else:
        return "Method not allowed", 405
