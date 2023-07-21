import time

from utils import func
from utils.path import ImagePath
from widgets import log


def fight_is_over():
    """
    判断游戏是否结束
    """
    pass


def wait_challenge_completed():
    """
    等待挑战成功
    """
    func.wait_image(ImagePath.CHALLENGE_COMPLETED, max_time=1800)
    log.transmitAllLog("挑战成功")
