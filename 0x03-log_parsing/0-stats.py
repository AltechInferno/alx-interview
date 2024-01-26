#!/usr/bin/python3
"""
Log parsing module
"""

import sys

def print_stats(stats, file_size):
    print("File size: {:d}".format(file_size))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))

def process_line(line, stats, file_size):
    nonlocal count
    count += 1
    data = line.split()
    try:
        status_code = data[-2]
        if status_code in stats:
            stats[status_code] += 1
    except IndexError:
        pass
    try:
        file_size += int(data[-1])
    except (IndexError, ValueError):
        pass
    if count % 10 == 0:
        print_stats(stats, file_size)
    return file_size

if __name__ == '__main__':
    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    try:
        for line in sys.stdin:
            filesize = process_line(line, stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise

