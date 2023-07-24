from flask import Flask, request, jsonify, send_file, request
from PIL import Image, ImageFont, ImageDraw
from geometry import Geometry
import json
from io import BytesIO


app = Flask(__name__)


@app.route('/')
def gt_image():
    img = Image.new('RGB', (1000, 1000), (0, 0, 0))

    pen = ImageDraw.Draw(img)

    text = "ALWAYS BE HAPPY(LAUGHING IS THE BEST MEDICINE)"

    pen.text

    Geometry.rectangle(pen, 100, 100, 200, 200, (255, 155, 0))
    Geometry.ellipse(draw=pen, x=100, y=100, height=200,
                     width=200, rbg=(255, 0, 0))
    Geometry.polygon(draw=pen, x=100, y=100, radius=100,
                     n_sites=7, rotation=0, rbg=(0, 255, 0))
    Geometry.text(draw=pen, x=100, y=100, size=100, text=text, words_per_line=30,
                  align="left", rgb=(255, 255, 255), font="sans-serif")

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
