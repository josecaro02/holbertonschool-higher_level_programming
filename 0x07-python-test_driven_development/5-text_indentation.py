#!/usr/bin/python3
''' Function that prints a text again but
adding 2 new lines if find the characters
'.' or '?'

'''


def text_indentation(text):
    ''' This function raise TypeError if the value givn
    is not a string.
    And Remove spaces at the beginnig or end of the lie
    '''
    if type(text) != str:
        raise TypeError('text must be a string')
    else:
        for i in range(len(text)):
            if text[i] == "." or text[i] == "?" or \
               text[i] == ":":
                print("{:s}\n".format(text[i]))
            elif text[i] == " " and (text[i - 1] == "." or \
                                     text[i - 1] == "?" or \
                                     text[i - 1] == ":"):
                    continue
            else:
                print("{:s}".format(text[i]), end="")
