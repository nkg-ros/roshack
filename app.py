from flask import Flask, render_template, make_response, send_file
import tile
import StringIO
import db
import os


app = Flask(__name__)

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

@app.route('/tile/<int:x>/<int:y>/<int:z>')
def tile_endpoint(x, y, z):
    if z > 5:
        no_data = CURRENT_PATH + '/static/img/no_data.png'
        print no_data
        #return send_file(no_data, mimetype="image/png")
        resp = flask.make_response(open(fullpath).read())
        resp.content_type = "image/jpeg"
        return resp

    data = db.get_tile_data(x, y, z)
    if data is None:
        print "NOPE"
        return make_response("Not found.", 404)
    else:
        image = tile.render_image(
            list(data['values']),
            z
        )

        tmp = StringIO.StringIO()

        image.save(tmp, format="PNG")
        tmp.seek(0, 0)

        return send_file(tmp, mimetype="image/png")


@app.route('/')
def home():
    return render_template(
        'home.html'
    )


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

