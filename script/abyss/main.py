import os
import shutil

import log
from config import abspath


class Abyss:
    @classmethod
    def run(cls):
        from Auto_Simulated_Universe.abyss import Abyss as Auto_Su_Abyss
        cls.check_file_exist()
        os.chdir(os.path.join(abspath, "Auto_Simulated_Universe"))
        abyss = Auto_Su_Abyss()
        abyss.start_abyss()
        os.chdir(abspath)

    @classmethod
    def config_to_auto_su_config(cls):
        """配队数据传递至abyss的info.yml"""
        pass

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
    Abyss.check_file_exist()
