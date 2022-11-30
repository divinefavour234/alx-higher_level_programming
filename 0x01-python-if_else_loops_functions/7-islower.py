#!/usr/bin/python3
def islower(c):
    ascII = ord(c)
    if ascII in range(97, 123):
        return True
    else:
        return False
