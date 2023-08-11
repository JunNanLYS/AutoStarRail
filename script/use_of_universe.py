import os

from Auto_Simulated_Universe import align_angle, states
from utils import tool, dialog
 

def run_align_angle():
    dialog.new_win_message("模拟宇宙",
                           "启动校准，模拟宇宙处于适配期，若遇BUG请见谅")
    os.chdir(os.path.join(tool.PathTool.get_root_path(), 'Auto_Simulated_Universe'))
    align_angle.main()
 

def run_states():
    dialog.new_win_message("模拟宇宙",
                           "运行自动模拟宇宙，请保证角色站在模拟宇宙台子上谢谢")
    os.chdir(os.path.join(tool.PathTool.get_root_path(), 'Auto_Simulated_Universe'))
    states.main()


if __name__ == '__main__':
    run_states()