#!/usr/bin/python3
"""
Log parsing Module
"""

import sys

if __name__ == '__main__':

    fileSize, count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {i: 0 for i in status_codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(fileSize))
        for i, j in sorted(stats.items()):
            if j:
                print("{}: {}".format(i, j))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                s_code = data[-2]
                if s_code in stats:
                    stats[s_code] += 1
            except BaseException:
                pass
            try:
                fileSize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, fileSize)
        print_stats(stats, fileSize)
    except KeyboardInterrupt:
        print_stats(stats, fileSize)
        raise
