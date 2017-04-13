"""Get the number of each character in any given text.
Inputs:
A txt file -- You will be asked for an input file. Simply input the name
of the txt file in which you have the desired text.
"""

import pprint
import collections


def main():

    file_input = raw_input('File Name: ')

    with open(file_input, 'r') as info:
        count = collections.Counter(info.read().upper())
        value = pprint.pformat(count)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(value)


if __name__ == "__main__":
    main()
