import json
import os
import sys


class PathTool:
    PROJECT_NAME = "AutoStarRail"

    @classmethod
    def get_root_path(cls) -> str:
        """
        :return: 项目根目录
        """
        cur_path: str = sys.argv[0]
        while cur_path.split('\\')[-1] != cls.PROJECT_NAME:
            cur_path = os.path.dirname(cur_path)
        return cur_path

    @classmethod
    def get_drives(cls):
        """
        :return: 当前电脑所有盘符
        """
        drives = []
        for drive in os.popen("fsutil fsinfo drives"):
            drives.extend(drive.split()[1:])
        return drives

    @classmethod
    def find_file(cls, name, path):
        """
        找文件
        :param name: 根目录 (C:\\, D:\\abc\\d)
        :param path: 要查找的文件名
        :return:
        """
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)


class JsonTool:
    @classmethod
    def get_config_json(cls) -> dict:
        """
        :return: 配置文件
        """
        path = os.path.join(PathTool.get_root_path(), "config.json")
        with open(path, 'r', encoding='UTF-8') as f:
            res = json.load(f)
        return res

    @classmethod
    def dump_config_json(cls, config: dict):
        """
        :param config: 配置文件
        """
        path = os.path.join(PathTool.get_root_path(), "config.json")
        with open(path, 'w', encoding='UTF-8') as f:
            json.dump(config, f)

