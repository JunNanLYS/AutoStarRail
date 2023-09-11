import os
import sys
import traceback
import log
from config import cfg, abspath
from script.utils.interface import UniverseUtils as Utiles

sys.path.append(os.path.join(abspath, "Auto_Simulated_Universe"))


class Universe:
    su = None

    @classmethod
    def run_universe(cls):
        from Auto_Simulated_Universe.states import SimulatedUniverse

        my_utiles = Utiles()
        my_utiles.start()
        my_utiles.into_universe()
        my_utiles.stop()
        # 改变工作目录，Auto_Simulated_Universe使用了大量相对路径
        os.chdir(os.path.join(abspath, "Auto_Simulated_Universe"))
        cls.config_to_auto_simulated_universe_config()
        cls.su = SimulatedUniverse(cfg.get(cfg.universe_find), cfg.get(cfg.universe_debug),
                                   cfg.get(cfg.universe_show_map), cfg.get(cfg.universe_speed),
                                   bonus=cfg.get(cfg.universe_bonus), update=cfg.get(cfg.universe_update))
        try:
            cls.su.start()
        except Exception:
            traceback.print_exc()
        finally:
            cls.su.stop()
        os.chdir(abspath)

    @classmethod
    def run_align_angle(cls):
        from Auto_Simulated_Universe import align_angle
        from utils.config import config  # 不这样导入就只有第一次校准有效
        os.chdir(os.path.join(abspath, "Auto_Simulated_Universe"))
        align_angle.main()
        cfg.set(cfg.universe_angle, config.multi)  # 更新角度误差
        os.chdir(abspath)

    @classmethod
    def stop_universe(cls):
        cls.su.stop()
        os.chdir(abspath)

    @classmethod
    def config_to_auto_simulated_universe_config(cls):
        """AutoStarRail to Auto_Simulated_Universe"""
        from config import cfg
        from Auto_Simulated_Universe.utils.config import config
        log.info("数据同步至Auto_Simulated_Universe")
        config.angle = cfg.get(cfg.universe_angle)
        config.fate = cfg.get(cfg.universe_fate)
        config.difficult = cfg.get(cfg.universe_difficult)

        config.speed_mode = cfg.get(cfg.universe_speed)
        config.debug_mode = cfg.get(cfg.universe_debug)
        config.show_map_mode = cfg.get(cfg.universe_show_map)
        config.force_update = cfg.get(cfg.universe_update)
        config.bonus = cfg.get(cfg.universe_bonus)

        config.save()


if __name__ == '__main__':
    log.info("universe模块测试")
    Universe.run_align_angle()
