#!/usr/bin/env python3

"""Write a script that reads stdin line by line and compute metrics"""

import sys
import re
from collections import defaultdict


def main():
    """
    Reads logs from standard input and generates reports
    Reports:
        * Prints log size after reading every 10 lines & at KeyboardInterrupt
    Raises:
        KeyboardInterrupt (Exception): handles this exception and raises it
    """

    input_format = re.compile(
        r'^(?P<ip>\S+) - \[(?P<date>.+)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)$'
    )

    line_read = 0
    total_size = 0
    status_counts = defaultdict(int)
    valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}

    try:
        for line in sys.stdin:
            line_read += 1

            # Match the line against the regex pattern
            match = input_format.match(line.strip())
            if not match:
                continue
            # Extract File size and status code
            size = int(match.group('size'))
            status = int(match.group('status'))

            total_size += size
            if status in valid_status_codes:
                status_counts[status] += 1

            if line_read % 10 == 0:
                print("File size: {}".format(total_size))
                for status in sorted(status_counts):
                    if status_counts[status] > 0:
                        print("{}: {}".format(status, status_counts[status]))

    except KeyboardInterrupt:
        raise


if __name__ == "__main__":
    main()
