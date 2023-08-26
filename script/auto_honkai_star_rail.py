"""
自动运行所有脚本
暂时不支持模拟宇宙
"""

from widgets import log
from script import use_of_stamina, use_of_commission, use_of_world, use_of_universe
from utils import tool

universe_count = 0  # 模拟宇宙计数


def dump_config_json(stamina, world):
    """
    将参数保存至配置文件
    """
    from config import config
    log.transmitRunLog("保存此次运行配置")
    config.auto['stamina'] = stamina
    config.auto['world'] = world
    config.dump()


def get_scripts(stamina, world):
    """
    :return: 获取每种脚本的方法以及参数
    """
    import config
    from config import config as config_instance
    scripts = {
        use_of_commission.run: (),
        use_of_stamina.run: (stamina,),
        use_of_world.run: (world,),
    }

    def yes():
        """
        沿用上一次运行配置
        """
        nonlocal scripts
        log.transmitRunLog("沿用上一次运行配置")
        stamina_param = config_instance.auto['stamina']
        world_param = config_instance.auto['world']
        scripts = {
            use_of_commission.run: (),
            use_of_stamina.run: (stamina_param,),
            use_of_world.run: (world_param,),
        }

    def no():
        """
        不使用上一次运行配置就直接保存这一次运行配置
        """
        log.transmitRunLog("使用新的运行配置")
        dump_config_json(stamina, world)
    if config.use_last_auto_config:
        yes()
    else:
        no()
    return scripts


def run(stamina_param: dict, world_param: str):
    """
    :param stamina_param: 参数
    :param world_param: 参数
    """
    scripts = get_scripts(stamina_param, world_param)
    log.transmitDebugLog(f"stamina_param: {stamina_param},  world_param: {world_param}", level=2)
    for method, args in scripts.items():
        method(*args)


if __name__ == "__main__":
    run({"calyx_1": 1}, "大矿区-1")
