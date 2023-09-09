import os

from config import abspath


class Abyss:
    @classmethod
    def run(cls):
        from Auto_Simulated_Universe.abyss import Abyss as auto_su_abyss
        os.chdir(os.path.join(abspath, "Auto_Simulated_Universe"))
        abyss = auto_su_abyss()
        abyss.start_abyss()
        os.chdir(abspath)

    @classmethod
    def config_to_auto_su_config(cls):
        """配队数据传递至abyss的info.yml"""
        pass
