#!/usr/bin/env python3


def main():
    find_sum('input1')


def find_sum(path):
    with open(path) as f:
        lines = [line.rstrip() for line in f]

    pairs = []
    for line in lines:
        pair = ''
        for char in line:
            if char.isnumeric():
                pair = pair+char
                break
        for char in reversed(line):
            if char.isnumeric():
                pair = pair+char
                break
        if pair != '':
            pairs.append(int(pair))

    number = sum(pairs)
    print(number)


if __name__ == "__main__":
    main()
