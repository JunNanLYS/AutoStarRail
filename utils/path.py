import os

from utils.tool import PathTool


class ImagePath:
    IMAGE_ROOT_PATH = os.path.join(PathTool.get_root_path(), "images\\")

    MANDATE = IMAGE_ROOT_PATH + r"mandate.png"  # 任务书
    BOOK = IMAGE_ROOT_PATH + r"book.png"  # 星际和平书
    INDEX = IMAGE_ROOT_PATH + r"index.png"  # 生存索引
    INDEX_SELECTED = IMAGE_ROOT_PATH + r"indexSelected.png"  # 选中状态下的"生存索引"

    CALYX_GOLD = IMAGE_ROOT_PATH + r"calyxGold.png"  # 花萼(金)
    CALYX_GOLD_SELECTED = IMAGE_ROOT_PATH + r"calyxGoldSelected.png"  # 选中的花萼(金)
    CALYX_CHARACTER_EXP = IMAGE_ROOT_PATH + r"calyxCharacterEXP.png"  # 花萼(角色经验)
    CALYX_CONE_EXP = IMAGE_ROOT_PATH + r"calyxConeEXP.png"  # 花萼(光锥经验)
    CALYX_CREDIT = IMAGE_ROOT_PATH + r"calyxCredit.png"  # 花萼(信用点)

    CALYX_RED = IMAGE_ROOT_PATH + r"calyxRed.png"  # 花萼(赤)
    CALYX_DESTRUCTION = IMAGE_ROOT_PATH + r"calyxDestruction.png"  # 毁灭行迹
    CALYX_PRESERVATION = IMAGE_ROOT_PATH + r'calyxPreservation.png'  # 存护行迹
    CALYX_HUNT = IMAGE_ROOT_PATH + r"calyxHunt.png"  # 巡猎行迹
    CALYX_ABUNDANCE = IMAGE_ROOT_PATH + r"calyxAbundance.png"  # 丰饶行迹
    CALYX_ERUDITION = IMAGE_ROOT_PATH + r"calyxErudition.png"  # 智识行迹
    CALYX_HARMONY = IMAGE_ROOT_PATH + r"calyxHarmony.png"  # 和谐行迹
    CALYX_NIHILITY = IMAGE_ROOT_PATH + r"calyxNihility.png"  # 虚无行迹

    CHALLENGE = IMAGE_ROOT_PATH + r"challenge.png"  # 副本的挑战按钮
    CHALLENGE_COMPLETED = IMAGE_ROOT_PATH + r"challengeCompleted.png"  # 挑战成功
    START_CHALLENGE = IMAGE_ROOT_PATH + r"startChallenge.png"  # 开始挑战按钮
    ADD_CHALLENGE = IMAGE_ROOT_PATH + r"addChallenge.png"  # 添加挑战副本的次数按钮
    TRANSMISSION = IMAGE_ROOT_PATH + r"transmission.png"  # 传送按钮

    START_GAME = IMAGE_ROOT_PATH + r"startGame.png"  # 启动器的开始游戏
    ENTER_GAME = IMAGE_ROOT_PATH + r"enterGame.png"  # 进入游戏
    EXIT_COPIES = IMAGE_ROOT_PATH + r"exitCopies.png"  # 退出挑战

