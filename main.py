# ~./.venv/bin/python

from instagrapi import Client
import os
from dotenv import load_dotenv

load_dotenv()


IG_USERNAME = os.environ.get("IG_USERNAME")
IG_PASSWORD = os.environ.get("IG_PASSWORD")
IG_CREDENTIAL_PATH = "./ig_settings.json"
SLEEP_TIME = "600"  # in seconds

cl = Client


class Bot:
    _cl = None

    def __init__(self):
        self._cl = Client()
        if os.path.exists(IG_CREDENTIAL_PATH):
            self._cl.load_settings(IG_CREDENTIAL_PATH)
            self._cl.login(IG_USERNAME, IG_PASSWORD)
        else:
            self._cl.login(IG_USERNAME, IG_PASSWORD)
            self._cl.dump_settings(IG_CREDENTIAL_PATH)
