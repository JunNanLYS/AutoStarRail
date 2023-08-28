import os
from typing import Dict, List

from utils import path

filename = path.ImagePath


def get_png(dir_path: str) -> List[str]:
    dir_path = ".\\images\\" + dir_path
    png_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.png'):
                png_files.append(os.path.join(root, file))
    return png_files


# key:模板图 value:场景图文件夹名
TEST_DATA: Dict[str, List[str]] = {
    filename.QUESTION_MASK: get_png("questionMask"),
    filename.WARNING: get_png("warning")
}
