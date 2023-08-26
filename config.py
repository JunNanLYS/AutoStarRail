import os
import json

from widgets import log

version = "0.6"
github_url = "https://github.com/zjnGitHub/AutoStarRail"
abspath = os.path.dirname(os.path.abspath(__file__))  # 项目绝对路径
use_last_auto_config = False  # 是否使用上一次运行配置


class Config(object):
    __instance = None
    __is_init = False

    def __init__(self):
        if not Config.__is_init:
            self.game_path = "D:/星穹铁道/Star Rail/launcher.exe"  # 游戏路径
            self.auto_fight = True  # 自动战斗
            self.use_fuel = False  # 使用燃料
            self.fuel_number = 1
            self.use_explore = False  # 使用星穹
            self.explore_number = 1
            self.auto = {}  # 一键自动，这里储存的是上一次配置
            self.angle = 1.0  # 角度误差
            self.load()
            Config.__is_init = True

    def load(self):
        """
        载入配置文件
        """
        filename = os.path.join(abspath, "config.json")
        with open(filename, "r", encoding="utf-8") as f:
            game_config = json.load(f)
        try:
            self.game_path = game_config["game_path"]
            self.auto_fight = game_config["auto_fight"]
            self.use_fuel = game_config["use_fuel"]
            self.fuel_number = game_config["fuel_number"]
            self.use_explore = game_config["use_explore"]
            self.explore_number = game_config["explore_number"]
            self.auto = game_config["auto"]
            self.angle = game_config["angle"]
            log.transmitDebugLog("config载入成功", level=2)
        except KeyError as e:
            log.transmitDebugLog(f"config载入失败，config.json缺少{e}", level=2)
            exit()
        except Exception:
            log.transmitDebugLog("出现莫名错误")
            exit()

    def dump(self):
        """
        存储配置文件
        """
        filename = os.path.join(abspath, "config.json")
        with open(filename, "w", encoding="utf-8") as f:
            game_config = {
                "game_path": self.game_path,
                "auto_fight": self.auto_fight,
                "use_fuel": self.use_fuel,
                "fuel_number": self.fuel_number,
                "use_explore": self.use_explore,
                "explore_number": self.explore_number,
                "auto": self.auto,
                "angle": self.angle
            }
            json.dump(game_config, f)

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


config = Config()
