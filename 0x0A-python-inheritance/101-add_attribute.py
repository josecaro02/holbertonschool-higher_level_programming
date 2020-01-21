#!/usr/bin/python3


def add_attribute(obj, name, value):
    try:
        setattr(obj, name, value)
    except:
        raise TypeError('can\'t add new attribute')
