import os
import json

from pydantic import BaseModel

from utils import tool
from StarRailAssistant.utils.config import sra_config_obj


class MapData(BaseModel):
    author: str
    filename: str
    name: str
    number: str


name_to_map = {}  # name: Map
number_to_map = {}  # number: Map

root_path = tool.PathTool.get_root_path()
map_filename = root_path + r'\StarRailAssistant\map'  # 地图文件地址

json_files = [file for file in os.listdir(map_filename) if file.endswith('.json')]

for json_file in json_files:
    json_filename = os.path.join(map_filename, json_file)
    with open(json_filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        map_number = json_file.split('.')[0].replace('map_', '')
        m = MapData(author=data['author'], filename=json_filename, name=data['name'], number=map_number)
        name_to_map[data['name']] = m
        number_to_map[map_number] = m

update_dict = {
    "脚本": {
        'skip_verify': False,
        'type': "star",
        'version': "main",
        'url_zip': f"https://github.com/{sra_config_obj.github_source}/StarRailAssistant/archive/refs/heads/main.zip",
        'unzip_path': ".",
        'keep_folder': ['.git', 'logs', 'picture', 'map', 'tmp', 'venv'],
        'keep_file': ['config.json', 'version.json', 'star_list.json', 'README_CHT.md', 'README.md'],
        'zip_path': "StarRailAssistant-main/",
        'name': "脚本",
        'delete_file': False
    },
    "地图": {
        'skip_verify': False,
        'type': "map",
        'version': "map",
        'url_zip': f"https://raw.githubusercontent.com/{sra_config_obj.github_source}/StarRailAssistant/map/map.zip",
        'unzip_path': "map",
        'keep_folder': [],
        'keep_file': [],
        'zip_path': "map/",
        'name': "地图",
        'delete_file': True
    },
    "图片": {
        'skip_verify': False,
        'type': "picture",
        'version': "map",
        'url_zip': f"https://raw.githubusercontent.com/{sra_config_obj.github_source}/StarRailAssistant/map/picture.zip",
        'unzip_path': "picture",
        'keep_folder': [],
        'keep_file': [],
        'zip_path': "map/",
        'name': "图片",
        'delete_file': True
    },
}

