#!/urs/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    length = length - 1
    if length != -1:
        for i in my_list:
            print("{}".format(my_list[length]))
            length = length - 1