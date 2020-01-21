#!/usr/bin/python3


class MyInt(int):

    def __eq__(self, other):
        return not other.__eq__(self)

    def __ne__(self, other):
        return other.__eq__(self)
