#!/usr/bin/python3
'''minimum operations coding challenge.
'''
def minOperations(n):
    '''this Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    count = 0
    cb = 0
    done = 1
    # print('H', end='')
    while done < n:
        if cb == 0:
            # initialized (the first copy all and paste)
            cb = done
            done += cb
            count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy and paste all
            cb = done
            done += cb
            count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif cb > 0:
            # paste
            done += cb
            count += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return count
