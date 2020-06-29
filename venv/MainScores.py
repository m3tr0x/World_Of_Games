# This file’s purpose is to retrieve the current user score from the scores.txt file over HTTP with
# HTML. This will be done by using python’s flask library.
# Methods
# 1. score_server() –
# This function will serve the score. It will read the score from the scores file and will return
# an HTML
#
# If the function will have a problem showing the result of reading the error it will return the
# ERROR_MESSAGE (from Utils.py) and the exception message

from flask import Flask
from Utils import scores_file_name, error
app = Flask('__name__')


@app.route('/')
def score_server():
    try:
        score = open(scores_file_name, "r")
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + error + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">""" + str(score.readline()) + """</div></h1>
        </body>
    </html>"""

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, threaded=True, port=5000)