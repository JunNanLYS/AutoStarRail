import unittest


class Test(unittest.TestCase):
    def test_angle(self):
        import data_angle
        from world.script import calculate_angle
        test_data = data_angle.TEST_DATA
        for p1, p2, ans in test_data:
            self.assertEqual(calculate_angle(p1, p2), ans)


if __name__ == '__main__':
    pass
