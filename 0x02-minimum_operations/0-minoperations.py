#!/usr/bin/python3
'''minimum operations coding challenge.
'''


def min_operations(n):
    """this Computes the fewest number of operations needed to result
    in exactly n H characs.
    """
    if not isinstance(n, int) or n <= 0:
        return 0

    operations_count = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0:
            # Initialization (the first copy all and paste)
            clipboard = done
            done += clipboard
            operations_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            # Copy all and paste
            clipboard = done
            done += clipboard
            operations_count += 2
        elif clipboard > 0:
            # Paste
            done += clipboard
            operations_count += 1

    return operations_count

# Example usage:
result = min_operations(10)
print(result)

