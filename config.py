import os

from qfluentwidgets import QConfig, ConfigItem, qconfig

import log

version = "0.6.0"
github_url = "https://github.com/JunNanLYS/AutoStarRail"
abspath = os.path.dirname(os.path.abspath(__file__))  # 项目绝对路径
use_last_auto_config = False  # 是否使用上一次运行配置


class Config(QConfig):
    """ Config of application """
    # game
    game_path = ConfigItem("game", "game_path", "D:/星穹铁道/Star Rail/launcher.exe")
    auto_fight = ConfigItem("game", "auto_fight", False)
    open_map = ConfigItem("game", "open_map", 'm')

    # stamina
    use_fuel = ConfigItem("stamina", "use_fuel", False)
    use_explore = ConfigItem("stamina", "use_explore", False)
    last_stamina = ConfigItem("stamina", "last", {})
    last_stamina_time = ConfigItem("stamina", "time", "2023年9月3日 21:03:46")

    # universe
    universe_angle = ConfigItem("universe", "angle", 1.0)
    universe_number = ConfigItem("universe", "number", 6)
    universe_count = ConfigItem("universe", "count", 1)
    universe_auto_angle = ConfigItem("universe", "auto_angle", False)
    universe_find = ConfigItem("universe", "find", 1)
    universe_debug = ConfigItem("universe", "debug", 0)
    universe_show_map = ConfigItem("universe", "show_map", 0)
    universe_update = ConfigItem("universe", "update", 0)
    universe_speed = ConfigItem("universe", "speed", 0)
    universe_bonus = ConfigItem("universe", "bonus", 0)
    universe_difficult = ConfigItem("universe", "difficulty", 3)
    universe_fate = ConfigItem("universe", "fate", "巡猎")

    # world
    world_angle = ConfigItem("world", "angle", 1.0)
    last_world = ConfigItem("world", "last", {})

    def save(self):
        log.info("保存成功")
        super().save()

    def set(self, item, value, save=True):
        log.info(f"设置{item.name}为{value}")
        super().set(item, value, save)

    @property
    def sum_stamina(self):
        """计算上一次设置的体力总值"""
        res = 0
        d = {"calyx": 10, "shadow": 30, "cavern": 40, "echo": 30}
        for name, cnt in self.last_stamina.value.items():
            for prefix, v in d.items():
                if prefix in name:
                    res += v * cnt
                    break
        return res


# 创建配置实例并使用配置文件来初始化它
cfg = Config()
qconfig.load(os.path.join(abspath, "config.json"), cfg)
log.info("Config载入成功")
log.info(f"版本号{version}")
log.info(f"该项目为公益开源项目，若从github外购买请立即差评并举报商家，github地址为{github_url}")
cfg.save()
