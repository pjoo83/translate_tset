from base.check_tools import start_check
from base.read_all_files import find_file
from base.check_tools import absolute_path


def test_check():
    """
        IOS内容检查
    """
    files = find_file(fr"{absolute_path('data/ios_data')}", include_str="language_ios",
                      filter_strs=[".~"])
    if len(files) > 1:
        start_check("ios")
        print('')
    else:
        print("ios_data文件中只有一个多语言文件，需要再下一份，保持文件夹中有两文件，就可以开始")
