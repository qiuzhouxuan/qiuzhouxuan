# 同时测试多个类
# unittest结合HTMLTestRunner可以生成html报告
import unittest


class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    # 测试之前的资源准备
    def setUp(self):
        print("set up")

    # 测试之后的资源清理
    def tearDown(self):
        print("tear down")

    def test_case01(self):
        # 断言两个是否相等
        self.assertEqual(2, 2, "断言是否相等")
        print("test_case01")

    # 跳过执行当前测试用例
    def test_case03(self):
        print("test_case03")

    def test_case04(self):
        print("test_case04")

    @unittest.skipIf(1 + 1 == 2, "跳过这条测试用例")
    def test_case02(self):
        print("test_case02")


class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print("test_demo1_case0")

    def test_demo1_case1(self):
        print("test_demo1_case1")


class demo2(unittest.TestCase):
    def test_demo2_case0(self):
        print("test_demo1_case0")

    def test_demo2_case1(self):
        print("test_demo2_case1")


if __name__ == '__main__':
    # 创建测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(demo)
    suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    suiteall = unittest.TestSuite([suite, suite1])
    # 添加执行的用例

    # 启动套件
    unittest.TextTestRunner().run(suiteall)
