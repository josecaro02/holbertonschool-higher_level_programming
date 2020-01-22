#!/usr/bin/python3


def class_to_json(obj):
    priv_att = '_' + obj.__class__.__name__
    test = {}
    for name in dir(obj):
        if name.startswith('_') and not name.startswith(priv_att):
            continue
        else:
            att = getattr(obj, name)
            if type(att) == int or type(att) == bool or type(att) == str\
               or type(att) == list or type(att) == dict:
                test[name] = att
    return (test)
