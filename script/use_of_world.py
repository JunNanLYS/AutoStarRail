import os

from widgets import log
from utils import dialog, tool
from script import start_game
from script.world import name_to_map, update_dict
from StarRailAssistant.run import run_map
from StarRailAssistant.utils.update_file import update_file


def run(map_name):
    start_game.run()
    log.transmitAllLog("运行锄大地")
    os.chdir(os.path.join(tool.PathTool.get_root_path(), 'StarRailAssistant'))
    number = name_to_map[map_name].number  # 获取地图编号
    run_map(number)
    log.transmitAllLog('运行完成')
    dialog.new_win_message("温馨提示", "锄大地运行完毕")


def update(target: str):
    if target != "全部":
        update_file().update_file_main(**update_dict[target])
    else:
        for update_data in list(update_dict.values()):
            update_file().update_file_main(**update_data)


if __name__ == '__main__':
    run("支援舱段-1")
