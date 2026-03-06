#app.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "빠르고 바쁜 현대인들을 위한 개인 맞춤형 뉴스 웹"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)