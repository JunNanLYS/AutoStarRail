import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)


class Logger:
    widget = None

    @classmethod
    def transmit(cls, message, filename, function, level=logging.DEBUG):
        if cls.widget is None:
            return
        level_to_str = {logging.DEBUG: "DEBUG", logging.INFO: "INFO",
                        logging.WARNING: "WARNING", logging.ERROR: "ERROR",
                        logging.CRITICAL: "CRITICAL"}
        level_str = level_to_str[level]
        m = f"[{level_str}] {get_time()} [{filename}({function})]: {message}"
        cls.widget.add.emit(m)


def get_stack():
    import inspect
    stack = inspect.stack()[2]
    return stack.filename, stack.function


def get_time():
    time = datetime.now()
    return time.strftime("%Y-%m-%d %H:%M:%S")


def info(mes):
    filename, function = get_stack()
    logging.info(f"{get_time()} [{filename}({function})]: {mes}")
    Logger.transmit(mes, filename, function, level=logging.INFO)


def debug(mes):
    filename, function = get_stack()
    logging.debug(f"{get_time()} [{filename}({function})]: {mes}")
    Logger.transmit(mes, filename, function, level=logging.DEBUG)


def warning(mes):
    filename, function = get_stack()
    logging.warning(f"{get_time()} [{filename}({function})]: {mes}")
    Logger.transmit(mes, filename, function, level=logging.WARNING)


def error(mes):
    filename, function = get_stack()
    logging.error(f"{get_time()} [{filename}({function})]: {mes}")
    Logger.transmit(mes, filename, function, level=logging.ERROR)


def critical(mes):
    filename, function = get_stack()
    logging.critical(f"{get_time()} [{filename}({function})]: {mes}")
    Logger.transmit(mes, filename, function, level=logging.CRITICAL)


def set_log_widget(widget):
    Logger.widget = widget


if __name__ == '__main__':
    info("test")
