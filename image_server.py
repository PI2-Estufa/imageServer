from nameko.rpc import rpc
import db
from db import Image
from psycopg2 import OperationalError


class ImageServer():
    name = "image_server"

    @rpc
    def receive_image(self, name):
        i = Image()
        i.url = name
        try:
            db.session.add(i)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return i.url
