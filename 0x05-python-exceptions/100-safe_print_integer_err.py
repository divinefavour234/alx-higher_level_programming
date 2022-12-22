#!/usr/bin/python3
def safe_print_integer_err(value):
     try:
        print("{:d}".format(value))
        return True
    except Exception:
        print("Exception: {} is not an integer".format(value), file=sys.stderr)
        return False
