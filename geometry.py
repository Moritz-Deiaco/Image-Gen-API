from PIL import ImageFont


class Geometry:

    @staticmethod
    def rectangle(draw, x: int, y: int, width: int, height: int, RBG: tuple):

        x2 = x + width
        y2 = y + height

        draw.rectangle((x, y, x2, y2), fill=(
            RBG[0], RBG[1], RBG[2]), outline=None)

    @staticmethod
    def ellipse(draw, x: int, y: int, width: int, height: int, RBG: tuple):

        x2 = x + width
        y2 = y + height

        draw.ellipse((x, y, x2, y2), fill=(
            RBG[0], RBG[1], RBG[2]), outline=None)

    @staticmethod
    def polygon(draw, x: int, y: int, radius: int, n_sites: int, rotation: int, RBG: tuple):

        x += radius
        y += radius

        draw.regular_polygon(bounding_circle=(x, y, radius), n_sides=n_sites,
                             rotation=rotation, fill=(
            RBG[0], RBG[1], RBG[2]), outline=None)

    @staticmethod
    def text(draw, x: int, y: int, size: int, RBG: tuple, font=None):

        if font != None and type(font) == str:
            if font == "serif":
                font = ImageFont.truetype(
                    filename='fonts/serif.ttf', size=size)

        draw.text()
