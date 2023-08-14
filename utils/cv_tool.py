def is_same_position(position1: tuple, position2: tuple, error_value: int):
    """
    传入两个坐标位置，判断这两个位置是否是同一个位置
    :param position1: 点1
    :param position2: 点2
    :param error_value: 误差值
    """
    for add_x in range(-error_value, error_value + 1):
        for add_y in range(-error_value, error_value + 1):
            if position1 == (position2[0] + add_x, position2[1] + add_y):
                return True
    return False


def remove_same_position(positions: list, error_value: int):
    flag = set()  # 记录需要被删除的下标
    cur = 0
    while cur < len(positions) - 1:
        nex = cur + 1
        while nex < len(positions):
            # 跳过被标记的下标
            if nex in flag:
                nex += 1
                continue
            # 判断是否是同一个点
            if is_same_position(positions[cur], positions[nex], error_value):
                flag.add(nex)
            nex += 1
        cur += 1
        # 跳过被标记的下标
        while cur in flag:
            cur += 1
    return [position for i, position in enumerate(positions) if i not in flag]


if __name__ == '__main__':
    pass
