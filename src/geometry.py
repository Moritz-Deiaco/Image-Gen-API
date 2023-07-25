from PIL import Image, ImageFont, ImageDraw
from textwrap import TextWrapper
from typing import Literal
from io import BytesIO

import requests
import validators


class Geometry:

    @staticmethod
    def rectangle(draw: ImageDraw, x: int, y: int, width: int, height: int, rgb: tuple[int, int, int]):

        x2 = x + width
        y2 = y + height

        draw.rectangle((x, y, x2, y2), fill=rgb, outline=None)

    @staticmethod
    def ellipse(draw: ImageDraw, x: int, y: int, width: int, height: int, rgb: tuple[int, int, int]):

        x2 = x + width
        y2 = y + height

        draw.ellipse((x, y, x2, y2), fill=rgb, outline=None)

    @staticmethod
    def polygon(draw: ImageDraw, x: int, y: int, radius: int, n_sites: int, rotation: int, rgb: tuple[int, int, int]):

        x += radius
        y += radius

        draw.regular_polygon(bounding_circle=(x, y, radius), n_sides=n_sites,
                             rotation=rotation, fill=rgb, outline=None)

    @staticmethod
    def text(draw: ImageDraw, x: int, y: int, size: int, text: str, words_per_line: int, align: Literal["left", "rigt", "center"], rgb: tuple[int, int, int], font: Literal["serif", "sans-serif", "monospace"] | None):

        if font != None and type(font) == str:
            if font == "serif":
                file = open("src/fonts/serif.ttf", "rb")
            elif font == "sans-serif":
                file = open("src/fonts/sans-serif.ttf", "rb")
            elif font == "monospace":
                file = open("src/fonts/mono.ttf", "rb")
        else:
            file = open("fonts/sans-serif.ttf", "rb")

        bytes_font = BytesIO(file.read())
        font = ImageFont.truetype(bytes_font, size)

        tw = TextWrapper()
        tw.width = words_per_line

        text = "\n".join(tw.wrap(text))

        draw.text((x, y), text, font=font, align=align, fill=rgb)

    @staticmethod
    def image(image_to_paste_on: Image, image_url: str, x: int, y: int, mask: bool, width: int, height: int):

        if not validators.url(image_url):
            return False
        else:
            r = requests.get(
                image_url, stream=True)
            image_formats = ("image/png", "image/jpeg", "image/jpg")
            if r.headers["content-type"] in image_formats:
                r.raw.decode_content = True
                image = Image.open(r.raw)

                if width != image.size[0] or height != image.size[1]:
                    image = image.resize((width, height))

                if mask:
                    image_to_paste_on.paste(image, (x, y), mask=image)
                else:
                    image_to_paste_on.paste(image, (x, y))
