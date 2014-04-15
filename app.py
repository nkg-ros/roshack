from flask import Flask, render_template, make_response, send_file
import tile
import StringIO


app = Flask(__name__)


@app.route('/tile/<string:x>/<string:y>/<string:z>')
def get_tile(x, y, z):
    image = tile.render_image(
        list(range(256*256))
    )

    tmp = StringIO.StringIO()

    image.save(tmp, format="PNG")
    tmp.seek(0, 0)

    return send_file(tmp, mimetype="png")


@app.route('/')
def home():
    return render_template(
        'home.html'
    )


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

