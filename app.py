from flask import Flask, render_template, make_response, send_file
import tile
import StringIO
import db


app = Flask(__name__)


@app.route('/tile/<int:x>/<int:y>/<int:z>')
def tile_endpoint(x, y, z):

    data = db.get_tile_data(x, y, z)
    if data is None:
        print "NOPE"
        return make_response("Not found.", 404)
    else:
        image = tile.render_image(
            list(data['values'])
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

