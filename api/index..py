from flask import Flask, Response
from pywebio.output import *
app = Flask(__name__)

#@app.route('/', defaults={'path': ''})
#@app.route('/<path:path>')
#def catch_all(path):
#    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
#   return Response(put_text('Awesome modifications!'), mimetype="text")
@app.route('/')
put_text('Hello Flaskies!')

if __name__ == '__main__':
    app.run()

