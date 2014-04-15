from flask import Flask, render_template


app = Flask(__name__)


@app.route('/tile/<string:x>/<string:y>/<string:z>')
def tile(x, y, z):
    return "tile %s %s %s" % (x, y, z)


@app.route('/')
def home():
    return render_template(
        'home.html'
    )


if __name__ == '__main__':
    app.run(debug=True)
