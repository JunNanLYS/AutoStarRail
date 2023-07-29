from StarRailAssistant.get_width import get_width
from StarRailAssistant.utils.calculated import calculated
from StarRailAssistant.utils.map import Map


def run_map(name='1-1_1'):
    game_title = "崩坏：星穹铁道"
    calculated(game_title, start=False)
    get_width(game_title)
    map = Map(game_title)
    map.auto_map(name)
