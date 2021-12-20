from __future__ import annotations

import argparse
import collections
import os.path

#import pytest

#import support

#INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
INPUT_TXT = 'data5.txt'
new_l = []
def compute(s: str) -> int:
    positions: collections.Counter[tuple[int, int]] = collections.Counter()
    lines = s.splitlines()
    for line in lines:
        """
        p1, p2 = line.split(' -> ')
        x1, y1 = support.parse_numbers_comma(p1)
        x2, y2 = support.parse_numbers_comma(p2)
        """
        data = str(line)
        p = data[0:len(data)-1].replace(' -> ',',').split(',')
        new_l.append((p))
        for i in range (0,len(new_l)):
            t = new_l[i]
            y1 = t[1]
            y2 = t[3]
            x1 = t[0]
            x2 = t[2]
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    positions[(x1, y)] += 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    positions[x, y1] += 1

    n = 0
    for k, v in positions.most_common():
        if v > 1:
            n += 1
        else:
            break
    return n

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f: #, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())