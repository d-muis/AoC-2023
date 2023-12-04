#!/usr/bin/env python3

from e1 import store_numbers


def main():

    with open('input1') as f:
        lines = [line.rstrip() for line in f]

    numbers = ('one','two','three','four','five','six','seven','eight','nine')
    dictionary = {number: str(index+1) for index, number in enumerate(numbers)}
    
    pairs = []
    for line in lines:
        num_list = get_num_list(line, dictionary)
        pairs.append(int(num_list[0]+num_list[-1]))
        
    solution = sum(pairs)
    print(solution)


def get_num_list(line, dictionary):
    
    num_list = ['' for i in range(len(line))]
    num_list = store_words_as_numbers(line, num_list, dictionary)
    num_list = store_numbers(line, num_list)

    num_list = [num for num in num_list if num != '']
    return num_list


def store_words_as_numbers(string, num_list, dictionary):
    for word, number in dictionary.items():
        index = string.find(word)
        while index != -1:
            num_list[index] = number
            index += 1
            index = string.find(word, index)
    return num_list 


if __name__ == "__main__":
    main()
