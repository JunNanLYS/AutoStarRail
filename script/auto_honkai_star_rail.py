"""
自动运行所有脚本
"""
from widgets import log
from script import use_of_stamina, use_of_commission, use_of_world

universe_count = 0  # 模拟宇宙计数


def run(stamina_param: dict, world_param: str):
    """
    传入参数时将按照参数来运行
    未传入参数时将按照配置文件运行
    配置文件为空时将不运行
    """
    scripts = {
        use_of_commission.run: (),
        use_of_stamina.run: (stamina_param,),
        use_of_world.run: (world_param,),
    }
    log.transmitDebugLog(f"stamina_param: {stamina_param},  world_param: {world_param}", level=2)
    for method, args in scripts.items():
        method(*args)


if __name__ == "__main__":
    run({"calyx_1": 1}, "大矿区-1")
