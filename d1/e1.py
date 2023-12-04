#!/usr/bin/env python3


def main():

    with open('input1') as f:
        lines = [line.rstrip() for line in f]

    pairs = []
    for line in lines:
        num_list = ['' for i in range(len(line))]
        num_list = store_numbers(line, num_list)
        num_list = [num for num in num_list if num != '']
        pairs.append(int(num_list[0]+num_list[-1]))

    solution = sum(pairs)
    print(solution)
    

def store_numbers(string, num_list):
    
    for i, char in enumerate(string):
        if char.isnumeric():
            print(char)
            num_list[i] = char
            print(num_list)

    return num_list


if __name__ == "__main__":
    main()
