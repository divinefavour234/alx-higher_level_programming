#!/usr/bin/python3
def uppercase(str):
    diff = ord('a') - ord('A')
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - diff)
        print("{}".format(c), end="")
    print("")
