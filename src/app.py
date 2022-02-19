from flask import Flask, render_template, request
from main import run_download


app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = b'_5#sssy2L"\n\xec]/'


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        data = request.form
        run_download(
            hash_tag=data["hashtag"],
            music_sound=data["sound"],
            user_name=data["username"],
        )
        return render_template("index.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    DEBUG = True
    HOST = "0.0.0.0"
    app.run(debug=DEBUG, host=HOST)
