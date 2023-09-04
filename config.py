import os

from qfluentwidgets import QConfig, ConfigItem, qconfig

import log

version = "0.6"
github_url = "https://github.com/zjnGitHub/AutoStarRail"
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

    # universe
    universe_angle = ConfigItem("universe", "angle", 1.0)
    universe_number = ConfigItem("universe", "number", 6)
    auto_angle = ConfigItem("universe", "auto_angle", False)
    last_universe = ConfigItem("universe", "last", {})

    # world
    world_angle = ConfigItem("world", "angle", 1.0)
    last_world = ConfigItem("world", "last", {})

    def save(self):
        log.info("保存成功")
        super().save()

    def set(self, item, value, save=True):
        log.info(f"设置{item}value为{value}")
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
