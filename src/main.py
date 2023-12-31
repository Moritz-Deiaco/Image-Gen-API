from flask import Flask, request, jsonify, send_file, request, abort
from PIL import Image, ImageFont, ImageDraw
from geometry import Geometry
import json
from io import BytesIO
import mysql.connector


app = Flask(__name__)


@app.route('/api/<image_id>')
def get_image(image_id):

    db = mysql.connector.connect(
        host="root02.oc.host.endelon.link",
        port="3306",
        user="imagegenapidb",
        passwd="7b3cehx5x17l",
        database="imagegenapidb"
    )

    cursor = db.cursor()

    cursor.execute(
        f"SELECT json_code FROM image_data WHERE image_id = {image_id} LIMIT 1")

    result = cursor.fetchall()

    data = json.loads(result[0][0])

    width = data["size"]["width"]
    height = data["size"]["height"]

    data_bgc = data["background-color"]

    bgcolor = (data_bgc["R"], data_bgc["G"], data_bgc["B"])

    img = Image.new('RGB', (width, height), bgcolor)

    pen = ImageDraw.Draw(img)

    geometry_data = data["geometry"]

    for geo_name, geo_data in data["geometry"].items():
        arr = geo_name.split("_")
        geo_name = arr[0]
        if geo_name == "rect":

            Geometry.rectangle(draw=pen, x=geo_data["x"], y=geo_data["y"], width=geo_data["width"],
                               height=geo_data["height"], rgb=(geo_data["color"]["r"], geo_data["color"]["g"], geo_data["color"]["b"]))
        elif geo_name == "ellipse":

            Geometry.ellipse(draw=pen, x=geo_data["x"], y=geo_data["y"], width=geo_data["width"],
                             height=geo_data["height"], rgb=(geo_data["color"]["r"], geo_data["color"]["g"], geo_data["color"]["b"]))
        elif geo_name == "polygon":

            Geometry.polygon(draw=pen, x=geo_data["x"], y=geo_data["y"], radius=geo_data["radius"],
                             n_sites=geo_data["sites"], rotation=geo_data["rotation"], rgb=(geo_data["color"]["r"], geo_data["color"]["g"], geo_data["color"]["b"]))

        elif geo_name == "text":

            httptext = request.args.get(geo_data["httpid"])
            if httptext:
                text = httptext
            else:
                text = geo_data["text"]

            Geometry.text(draw=pen, x=geo_data["x"], y=geo_data["y"], size=geo_data["size"], text=text, words_per_line=geo_data["words_per_line"],
                          align=geo_data["align"], rgb=(geo_data["color"]["r"], geo_data["color"]["g"], geo_data["color"]["b"]), font=geo_data["font_style"])
        elif geo_name == "image":

            httpurl = request.args.get(geo_data["httpid"])
            if httpurl:
                url = httpurl
            else:
                url = geo_data["image_url"]

            httpw = request.args.get(geo_data["httpid"]+"_w")
            if httpw:
                width = int(httpw)
            else:
                width = geo_data["width"]

            httph = request.args.get(geo_data["httpid"]+"_h")
            if httph:
                height = int(httph)
            else:
                height = geo_data["height"]

            httpx = request.args.get(geo_data["httpid"]+"_x")
            if httpx:
                x = int(httpx)
            else:
                x = geo_data["x"]

            httpy = request.args.get(geo_data["httpid"]+"_y")
            if httpy:
                y = int(httpy)
            else:
                y = geo_data["y"]

            httpt = request.args.get(geo_data["httpid"]+"_t")
            if httpt:

                if int(httpt) == 1:
                    t = True
                else:
                    t = False
            else:
                t = geo_data["transparent"]

            Geometry.image(
                img, url, x, y, t, width, height)

        else:
            continue

    image_binary = BytesIO()
    img.save(image_binary, "PNG")
    image_binary.seek(0)

    return send_file(
        image_binary,
        mimetype='image/png',
        as_attachment=False,
    )


if __name__ == "__main__":
    app.run(port="6969", debug=True)
