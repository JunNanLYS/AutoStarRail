import os

import config

from winotify import Notification


def win_message(title, content):
    Notification(
        app_id="AutoStarRail", title=title, msg=content,
        icon=os.path.join(config.abspath, r"doc\help.ico")
    ).show()


if __name__ == '__main__':
    win_message("Test", "Hello World")
