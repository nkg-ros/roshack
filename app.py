from flask import Flask, render_template, make_response
import tile


app = Flask(__name__)


@app.route('/tile/<string:x>/<string:y>/<string:z>')
def get_tile(x, y, z):
    image = tile.render_image(
        list(range(256*256))
    )

    response = make_response(image.tostring())
    response.headers['Content-Type'] = 'image/png'
    return response


@app.route('/')
def home():
    return render_template(
        'home.html'
    )


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

