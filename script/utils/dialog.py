from plyer import notification


def win_message(title, content):
    notification.notify(
        title=title,
        message=content,
        app_name="AutoStarRail",
    )


if __name__ == '__main__':
    win_message("Test", "Hello World")
