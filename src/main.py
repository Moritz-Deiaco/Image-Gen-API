from flask import Flask, request, jsonify, send_file
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from geometry import Geometry

from io import *


app = Flask(__name__)


@app.route('/')
def gt_image():
    img = Image.new('RGB', (1000, 1000), (0, 0, 0))

    font = ImageFont.truetype(filename='msyhbd.ttf', size=30)

    pen = ImageDraw.Draw(img)

    Geometry.rectangle(pen, 100, 100, 200, 200, (255, 155, 0))
    Geometry.ellipse(pen, 100, 100, 200, 200, (255, 0, 0))
    Geometry.polygon(pen, 100, 100, 100, 6, 0, (0, 255, 0))

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
