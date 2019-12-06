import time

from neobolt.exceptions import ServiceUnavailable
from neomodel import db, config
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    """Pause app untill graphdb is up and running"""

    def handle(self, *args, **kwargs):
        """Handle the command"""
        while True:
            try:
                db.set_connection(config.DATABASE_URL)
                self.stdout.write("Graph databse available!!!")
                break
            except ServiceUnavailable:
                self.stdout.write("Graph databse unavailable, waiting for 1 second...")
                time.sleep(1)






