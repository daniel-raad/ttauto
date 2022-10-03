from flask import Flask, render_template, request
from main import run_download
import threading

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = b'_5#sssy2L"\n\xec]/'


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        data = request.form
        print(data)
        run_download(hash_tag=data['hash_tag'])
        thread = threading.Thread(target=run_download, name="Downloader", kwargs=data)
        thread.start()
        return render_template("index.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    HOST = "0.0.0.0"
    app.run(debug=True, host=HOST)
