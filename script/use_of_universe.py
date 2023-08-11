import os

from Auto_Simulated_Universe import align_angle, states
from utils import tool
 

def run_align_angle():
    os.chdir(os.path.join(tool.PathTool.get_root_path(), 'Auto_Simulated_Universe'))
    align_angle.main()
 

def run_states():
    os.chdir(os.path.join(tool.PathTool.get_root_path(), 'Auto_Simulated_Universe'))
    states.main()


if __name__ == '__main__':
    run_states()