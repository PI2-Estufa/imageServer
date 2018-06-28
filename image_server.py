from nameko.rpc import rpc
import db
from db import Image


class ImageServer():
    name = "image_server"

    @rpc
    def receive_image(self, name):
        i = Image()
        i.url = name
        db.session.add(i)
        db.session.commit()
        return i.url
