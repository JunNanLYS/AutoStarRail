import os

from widgets import log
from script.start_game import start_game
from script.world import name_to_map, update_dict
from StarRailAssistant.run import run_map
from StarRailAssistant.utils.update_file import update_file


def run(map_name):
    start_game()
    log.transmitAllLog("运行锄大地")
    os.chdir(r'F:\AutoStarRail\StarRailAssistant')
    number = name_to_map[map_name].number  # 获取地图编号
    run_map(number)
    log.transmitAllLog('运行完成')


def update(target: str):
    if target != "全部":
        update_file().update_file_main(**update_dict[target])
    else:
        for update_data in list(update_dict.values()):
            update_file().update_file_main(**update_data)
