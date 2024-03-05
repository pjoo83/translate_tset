import unittest
from base.read_all_files import find_file
from base.check_tools import start_check
from base.testing import TestingCase


class TeslFlowServer(TestingCase):

    def test_check(self):
        """
            服务端内容检查
        """
        self.getDriver.close_page()
        files = find_file("../data/flutter_data", include_str="language_flutter", filter_strs=[".~"])
        print(files)
        if len(files) > 1:

            start_check("flutter")
        else:
            print("flutter_data文件中只有一个多语言文件，需要再下一份，保持文件夹中有两文件，就可以开始")


if __name__ == '__main__':
    suit = unittest.TestSuite()
    case = TeslFlowServer("test_case_flutter")
    suit.addTest(case)
    runner = unittest.TextTestRunner()
    runner.run(suit)
