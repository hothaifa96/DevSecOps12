import os
from flask import Flask

app = Flask(__name__)

#color = "red";
color = os.environ.get('APP_COLOR')

@app.route("/")
def main():
    return f'<html><body style="background:{color}"><h1><b>Welcome flask user!</b></h1></body></html>';

app.run(host="0.0.0.0", port=8080);
