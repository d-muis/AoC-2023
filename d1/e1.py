#!/usr/bin/env python3


def main():

    dictionary = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"}

    number = find_sum('input1', dictionary)
    print(number)


def find_occurrences(substring, string):
    
    index_list = []
    index = 0
    while index != -1:
        index = string.find(substring, index)
        if index != -1:
            index_list.append(index)
            index += 1
    return index_list

def replace_at_index(string, replacement, index):
    string = string[:index] + replacement + string[index+1:]
    return string

def insert_at_index(string, insertion, index):
    string = string[:index] + insertion + string[index:]
    return string

def find_sum(path, dictionary):
    
    with open(path) as f:
        lines = [line.rstrip() for line in f]

    pairs = []
    
    for line in lines:

        index_list_list = []

        #print(line)

        for k, v in dictionary.items():
            index_list = find_occurrences(k, line)
            index_list_list.append(index_list)
        for i, (k, v) in enumerate(dictionary.items()):
            for index in index_list_list[i]:
                line = replace_at_index(line, v, index)

            #for i, index in enumerate(index_list):
            #    line = insert_at_index(line, v, index+i)

        #print(line)

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

    #print(pairs)
    return sum(pairs)


if __name__ == "__main__":
    main()
