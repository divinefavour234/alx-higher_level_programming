#!/usr/bin/python3
def islower(c):
    ascII = ord(c)
    if ascII in range(67, 123):
        return True
    else:
        return False
