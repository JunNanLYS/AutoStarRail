import os
from enum import Enum
import json

from qfluentwidgets import QConfig, ConfigItem, RangeConfigItem, OptionsConfigItem, OptionsValidator, EnumSerializer

import log

version = "0.6"
github_url = "https://github.com/zjnGitHub/AutoStarRail"
abspath = os.path.dirname(os.path.abspath(__file__))  # 项目绝对路径
use_last_auto_config = False  # 是否使用上一次运行配置


class GameConfig(Enum):
    path = "path"


class MvQuality(Enum):
    FULL_HD = "Full HD"
    HD = "HD"
    SD = "SD"
    LD = "LD"

    @staticmethod
    def values():
        return [q.value for q in MvQuality]


class Config(QConfig):
    def __init__(self):
        super().__init__()
        self.onlineMvQuality = OptionsConfigItem("Online", "MvQuality", MvQuality.FULL_HD,
                                                 OptionsValidator(MvQuality), EnumSerializer(MvQuality))

    def load(self, file=None, config=None):
        super().load(file, config)
        log.info("已加载config")


cfg = Config()
cfg.load(os.path.join(abspath, "config.json"), cfg)
print(cfg.get(cfg.onlineMvQuality))
