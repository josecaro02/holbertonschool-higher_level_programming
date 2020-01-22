#!/usr/bin/python3
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

file_name = "add_item.json"
len_argv = len(sys.argv)
try:
    my_list = load_from_json_file("add_item.json")
    for i in range(1, len_argv):
        my_list.append(sys.argv[i])
except:
    my_list = []
finally:
    save_to_json_file(my_list, "add_item.json")
