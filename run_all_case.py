# coding=utf-8
import unittest

from unittest import defaultTestLoader
# 测试用例存放路径
case_path = 'case'


# 获取所有测试用例
def get_allcase():

    discover = defaultTestLoader.discover(case_path, pattern="test*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite


#
if __name__ == '__main__':
    # 运行测试用例
    runner = unittest.TextTestRunner()
    runner.run(get_allcase())

# print(get_allcase())
