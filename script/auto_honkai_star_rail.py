"""
自动运行所有脚本
"""
from script import use_of_stamina, use_of_commission, use_of_world

universe_count = 0  # 模拟宇宙计数


def run(stamina_param, world_param):
    scripts = {
        use_of_commission.run, (),
        use_of_stamina.run, (stamina_param, ),
        use_of_world.run, (world_param, ),
    }
    for method, args in scripts:
        method(*args)
