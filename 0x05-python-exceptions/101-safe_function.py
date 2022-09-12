#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        r = fct(*args)
        return 
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
