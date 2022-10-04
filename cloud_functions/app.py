from flask import Flask, request
from main import run_download

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = b'_5#sssy2L"\n\xec]/'


@app.route("/tiktok", methods=["POST"])
def index():
    data = request.get_json() 
    run_download(hash_tag=data['hash_tag'])
    return 'Downloading video', 204

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    HOST = "0.0.0.0"
    app.run(debug=False, host=HOST, port=8080)
