import unittest


class Test(unittest.TestCase):
    def test_angle(self):
        import data_angle
        from world.script import calculate_angle
        test_data = data_angle.TEST_DATA
        for p1, p2, ans in test_data:
            self.assertEqual(ans, calculate_angle(p1, p2))

    def test_template(self):
        """
        在测试文件下有一个images，里面存放有用于测试的图片
        这个测试主要测试模板图能否在大部分场景下正确识别
        """
        import cv2
        import data_template

        test_data = data_template.TEST_DATA
        for template_f, img_lis in test_data.items():
            template = cv2.imread(template_f)
            for img_f in img_lis:
                img = cv2.imread(img_f)
                res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, _ = cv2.minMaxLoc(res)
                self.assertTrue(max_val >= 0.8, f"{template_f}匹配值小于0.8")


class RoleTest(unittest.TestCase):
    def test_set_angle(self):
        from world.script import Map
        from utils.role import Role
        from utils.func import to_game_main
        m = Map()
        m.capture_atlas()
        to_game_main()
        Role.get_angle(m.big_map)
        angles = [90, 180]
        for angle in angles:
            Role.set_angle(Role.angle, angle)
            m.capture_atlas()
            to_game_main()
            cur = Role.get_angle(m.big_map)
            self.assertEqual(angle, cur)


if __name__ == '__main__':
    pass
