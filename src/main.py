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
    Geometry.ellipse(pen, 100, 100, 200, 200, (255, 0, 0))
    Geometry.polygon(pen, 100, 100, 100, 7, 0, (0, 255, 0))
    Geometry.text(pen, 100, 100, 20, text, 30,
                  "left", (255, 255, 255), "sans-serif")

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
