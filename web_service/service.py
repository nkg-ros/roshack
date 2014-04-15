from flask import Flask


app = Flask(__name__)


@app.route('/tile/<string:x>/<string:y>/<string:z>')
def tile(x, y, z):
    return "tile %s %s %s" % (x, y, z)


if __name__ == '__main__':
    app.run(debug=True)
