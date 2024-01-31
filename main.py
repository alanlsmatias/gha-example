import argparse
from datetime import datetime

def args_parser():
    parser = argparse.ArgumentParser(prog='SquaredDifference')
    parser.add_argument('-x', dest='x', type=int, default=1)
    parser.add_argument('-y', dest='y', type=int, default=1)
    return parser

def squared_diff(x: int, y: int):
    return (x - y) ** 2

if __name__ == '__main__':
    args = args_parser().parse_args()
    current_date = datetime.utcnow().date().isoformat()
    result = squared_diff(args.x, args.y)
    print(f'{current_date}: {result:.2f}')
