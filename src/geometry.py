from PIL import ImageFont
from textwrap import TextWrapper
from typing import Literal
from io import BytesIO


class Geometry:

    @staticmethod
    def rectangle(draw, x: int, y: int, width: int, height: int, rbg: tuple[int, int, int]):

        x2 = x + width
        y2 = y + height

        draw.rectangle((x, y, x2, y2), fill=rbg, outline=None)

    @staticmethod
    def ellipse(draw, x: int, y: int, width: int, height: int, rbg: tuple[int, int, int]):

        x2 = x + width
        y2 = y + height

        draw.ellipse((x, y, x2, y2), fill=rbg, outline=None)

    @staticmethod
    def polygon(draw, x: int, y: int, radius: int, n_sites: int, rotation: int, rbg: tuple[int, int, int]):

        x += radius
        y += radius

        draw.regular_polygon(bounding_circle=(x, y, radius), n_sides=n_sites,
                             rotation=rotation, fill=rbg, outline=None)

    @staticmethod
    def text(draw, x: int, y: int, size: int, text: str, words_per_line: int, align: Literal["left", "rigt", "center"], rbg: tuple[int, int, int], font: Literal["serif", "sans-serif", "monospace"] | None):

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

        draw.text((x, y), text, font=font, align=align, fill=rbg)
