from flask import Flask, request, jsonify, send_file, request
from PIL import Image, ImageFont, ImageDraw
from geometry import Geometry
import json
from io import BytesIO


app = Flask(__name__)


@app.route('/')
def get_image():

    data = json.load(open('src/test.json'))

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

            Geometry.text(draw=pen, x=geo_data["x"], y=geo_data["y"], size=geo_data["size"], text=geo_data["text"], words_per_line=geo_data["words_per_line"],
                          align=geo_data["align"], rgb=(geo_data["color"]["r"], geo_data["color"]["g"], geo_data["color"]["b"]), font=geo_data["font_style"])

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
    app.run(debug=True)
