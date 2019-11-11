from pathlib import Path
import argparse


def showdir(path: str = '.', all=False, detail=False, human=False):
    p = Path(path)
    for file in p.iterdir():
        yield file.name


parser = argparse.ArgumentParser(prog='ls',
                                 add_help=False,
                                 description='list your dirs'
                                 )  # 构造解析器
parser.add_argument('path', nargs='?', default='.')  # 位置参数
parser.add_argument('-l', action='store_true')  #
parser.add_argument('-h', action='store_true')  #
parser.add_argument('-a', '--all', action='store_true')  #
# showdir('E:\io')
if __name__ == '__main__':
    # showdir('E:\io')
    args = parser.parse_args(("E:\io", '-lah'))
    parser.print_help()
    print("args=", args)
    print(args.path, args.l, args.h, args.all)

    for file in showdir(args.path):
        print(file)
