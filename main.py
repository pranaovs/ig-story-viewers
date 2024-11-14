#!./.venv/bin/python

from instagrapi import Client
import os
from dotenv import load_dotenv
from instagrapi.types import Story, UserShort

load_dotenv()


IG_USERNAME = os.environ.get("IG_USERNAME")
IG_PASSWORD = os.environ.get("IG_PASSWORD")
IG_CREDENTIAL_PATH = "./ig_settings.json"
SLEEP_TIME = "600"  # in seconds


class Bot:
    _cl = None

    def __init__(self):
        self._cl = Client()
        if os.path.exists(IG_CREDENTIAL_PATH):
            self._cl.load_settings(IG_CREDENTIAL_PATH)  # type: ignore
            self._cl.login(IG_USERNAME, IG_PASSWORD)
        else:
            self._cl.login(IG_USERNAME, IG_PASSWORD)
            self._cl.dump_settings(IG_CREDENTIAL_PATH)  # type: ignore

    def get_self_stories(self):
        # print(self._cl.account_info())
        story_list: list[Story] = self._cl.user_stories(self._cl.account_info().pk)
        return story_list

    def get_story_viewers(self):
        story_list = self.get_self_stories()
        story_viewers: list[UserShort] = []
        for story in story_list:
            story_viewers.append(self._cl.story_viewers(story.pk))
        return story_viewers

    def get_story_viewer_names(self):
        story_list = self.get_self_stories()
        story_viewers: list[str] = []
        for story in story_list:
            user_list = self._cl.story_viewers(story.pk)
            for user in user_list:
                story_viewers.append(user.full_name)
        return story_viewers


def main():
    goodbot = Bot()
    print(goodbot.get_story_viewer_names())


if __name__ in "__main__":
    print("===========\n\n")
    main()
    print("\n\n===========")
