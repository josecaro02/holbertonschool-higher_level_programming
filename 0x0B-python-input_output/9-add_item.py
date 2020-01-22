#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    load_from_json = __import__('8-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

    file_name = "add_item.json"
    len_argv = len(sys.argv)
    try:
        my_list = load_from_json("add_item.json")
        for i in range(1, len_argv):
            my_list.append(sys.argv[i])
        save_to_json_file(my_list, "add_item.json")

    except:
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write("[]")
