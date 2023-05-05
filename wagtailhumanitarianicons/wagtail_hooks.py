import json
import os

from wagtail import hooks

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ICONS_LIST_PATH = os.path.join(BASE_DIR, "icons.json")


@hooks.register("register_icons")
def register_icons(icons):
    with open(ICONS_LIST_PATH, "r") as f:
        humanitarian_icons = json.load(f)
        for icon in humanitarian_icons:
            icons.append("wagtailhumanitarianicons/icons/{}".format(icon))
    return icons
