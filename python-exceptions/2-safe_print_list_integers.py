#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list if they are integers."""
    count = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass  # skip non-integers silently
        except IndexError:
            break  # stop if index out of range
        i += 1
    print()
    return count

