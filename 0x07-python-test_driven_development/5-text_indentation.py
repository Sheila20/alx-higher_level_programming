#!/usr/bin/python3
"""
    5-text_indentation.py
    Function that prints a text with 2 new lines after each of \
    these characters: ., ? and :
    return None
"""


def text_indentation(text):
    """ Function that prints a text with 2 new lines after each \
        of these characters: ., ? and :
        return None
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    f = 1
    for num, i in enumerate(text):
        if f == 1:
            if i == ' ' or i == '\t' or i == '\n':
                if text[num + 1] != ' ' and \
                   text[num + 1] != '\t' and text[num + 1] != '\n':
                    f = 0
                continue
            else:
                print("{:s}".format(i), end='')
                f = 0
        else:
            print("{:s}".format(i), end='')

        if i == '.' or i == '?' or i == ':':
            print("")
            print("")
            f = 1
