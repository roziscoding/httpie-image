import os
import sys
import io
from httpie.plugins import ConverterPlugin
from httpie.output.streams import BinarySuppressedError
from PIL import Image
from term_image.image import KittyImage

class ImagePlugin(ConverterPlugin):

    def convert(self, content_bytes):
        bytes = io.BytesIO(content_bytes)
        img = Image.open(bytes)
        image = KittyImage(img)
        image.draw()
        return 'image/*', ''

    @classmethod
    def supports(cls, mime):
        if mime.startswith('image/'):
            return True
        return False

    @classmethod
    def is_iterm2(cls):
        return os.environ.get('TERM_PROGRAM') == 'iTerm.app'
