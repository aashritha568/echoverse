from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        if text.strip() != "":
            tts = gTTS(text)
            filename = "static/output.mp3"
            tts.save(filename)
            return render_template("index.html", audio_file=filename)
    return render_template("index.html", audio_file=None)

if __name__ == '__main__':
    app.run(debug=False)