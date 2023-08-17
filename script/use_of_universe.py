import os
import traceback
from typing import Optional

from Auto_Simulated_Universe import align_angle, states
from utils import tool, dialog
from widgets import log


universe: Optional[states.SimulatedUniverse] = None


def run_align_angle():
    dialog.new_win_message("模拟宇宙",
                           "启动校准，模拟宇宙处于适配期，若遇BUG请见谅")
    os.chdir(os.path.join(tool.PathTool.get_root_path(), 'Auto_Simulated_Universe'))
    align_angle.main()


def run_states():
    global universe
    dialog.new_win_message("模拟宇宙",
                           "运行自动模拟宇宙，请保证角色站在模拟宇宙台子上谢谢")
    universe = states.SimulatedUniverse(find=1, debug=0, show_map=0, update=0, speed=0, bonus=0)
    os.chdir(os.path.join(tool.PathTool.get_root_path(), 'Auto_Simulated_Universe'))
    try:
        universe.start()
    except Exception:
        traceback.print_exc()
    finally:
        universe.stop()
        dialog.new_win_message("模拟宇宙",
                               "模拟宇宙自动化结束")


def stop_states():
    if universe is None:
        log.transmitRunLog(f"universe为None，只有在模拟宇宙自动化开启时才有效")
        return
    log.transmitRunLog("暂停模拟宇宙")
    universe.stop()
    dialog.new_win_message("模拟宇宙",
                           "暂停模拟宇宙")


if __name__ == '__main__':
    run_states()
