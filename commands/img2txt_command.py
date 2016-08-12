from api.command import Command
from PIL import Image
from bisect import bisect
import random

class Img2Txt(Command):

    client = None
    grayscale = [
        " ",
        " ",
        ".,-",
        "_ivc=!/|\\~",
        "gjez2]/(YL)t[+T7Vf",
        "mdK4ZGbNDXY5P*Q",
        "W8KMA",
        "#%$"
    ]
    zonebounds=[36,72,108,144,180,216,252]

    def __init__(self, client):
        super().__init__('Convert iamge to ascii', '[url]', ['img2txt', 'conv', 'convert'], [])
        self.client = client
        pass

    async def onCommand(self, message, args):
