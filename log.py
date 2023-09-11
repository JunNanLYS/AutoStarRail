import logging
from datetime import datetime

auto_sr = logging.getLogger("")
auto_sr.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
auto_sr.addHandler(stream_handler)


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
    auto_sr.info(f"{get_time()} [{filename}({function})]: {mes}")
    Logger.transmit(mes, filename, function, level=logging.INFO)


def debug(mes):
    filename, function = get_stack()
    auto_sr.debug(f"{get_time()} [{filename}({function})]: {mes}")
    Logger.transmit(mes, filename, function, level=logging.DEBUG)


def warning(mes):
    filename, function = get_stack()
    auto_sr.warning(f"{get_time()} [{filename}({function})]: {mes}")
    Logger.transmit(mes, filename, function, level=logging.WARNING)


def error(mes):
    filename, function = get_stack()
    auto_sr.error(f"{get_time()} [{filename}({function})]: {mes}")
    Logger.transmit(mes, filename, function, level=logging.ERROR)


def critical(mes):
    filename, function = get_stack()
    auto_sr.critical(f"{get_time()} [{filename}({function})]: {mes}")
    Logger.transmit(mes, filename, function, level=logging.CRITICAL)


def set_log_widget(widget):
    Logger.widget = widget


if __name__ == '__main__':
    info("test")
    debug("test")
    warning("test")
    error("test")
    critical("test")
    pass
