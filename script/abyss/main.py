import os
import shutil

import log
import game
from config import abspath
from script.utils.interface import AbyssUtils


class Abyss:
    @classmethod
    def run(cls):
        from Auto_Simulated_Universe.abyss import Abyss as Auto_Su_Abyss
        cls.check_file_exist()
        cls.config_to_auto_su_config()
        game.set_foreground()
        abyss_utils = AbyssUtils()
        abyss_utils.start()
        abyss_utils.into_abyss()
        abyss_utils.stop()

        os.chdir(os.path.join(abspath, "Auto_Simulated_Universe"))
        abyss = Auto_Su_Abyss()
        abyss.start_abyss()
        os.chdir(abspath)

    @classmethod
    def config_to_auto_su_config(cls):
        """配队数据传递至abyss的info.yml"""
        import yaml
        from config import cfg
        path = os.path.join(abspath, r"Auto_Simulated_Universe\abyss\info.yml")
        with open(path, 'w', encoding='utf-8') as f:
            d = {
                "order_text": cfg.get(cfg.abyss_list)
            }
            yaml.dump(d, f)

    @classmethod
    def check_file_exist(cls):
        path = os.path.join(abspath, r"Auto_Simulated_Universe\abyss\info_example.yml")
        target = os.path.join(abspath, r"Auto_Simulated_Universe\abyss\info.yml")
        if not os.path.exists(target):
            try:
                log.debug("info.yml不存在，复制info_example.yml")
                shutil.copyfile(path, target)
            except Exception as e:
                log.error("info_example.yml不存在，自己创建一个")
                # 有点懒，有空再写     0。0
                pass
        else:
            log.debug("info.yml存在")


if __name__ == "__main__":
    Abyss.run()
