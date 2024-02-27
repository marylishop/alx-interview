#!/usr/bin/python3

"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
 <status code> <file size> (if the format is not this one, the
 178.10.226.186 - [2023-12-21 21:58:06.848107] "GET /projects/260
   HTTP/1.1" 405 33
 line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size>
    (see input format above)
    Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405
          and 500
        if a status code doesn’t appear or is not an integer, don’t
          print anything for this status code
        format: <status code>: <number>
        status codes should be printed in ascending order
Warning: In this sample, you will have random value - it’s normal
 to not have the same output as this one.
"""

import sys


def printer(stats: dict, file_size: int) -> None:
    """ Function to print statistics """
    print("File size: {:d}".format(file_size))

    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


def function() -> None:
    """ Stdin processing function """
    # Initialize variables for file size and line count
    line_count, file_size = 0, 0
    # List of status codes to track
    stat_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    # Dictionary to store count for each status code
    stat_count = {k: 0 for k in stat_codes}

    try:
        # Iterate through each line from stdin
        for line in sys.stdin:
            # Increment line count
            line_count += 1

            # Split the line by spaces into a list of words
            data = line.split()
            # print(data)

            try:
                # Attempt to extract the status code from the line
                # Position; before last
                status_code = data[-2]

                # If the status code is in the list; update count
                if status_code in stat_count:
                    stat_count[status_code] += 1
            except Exception:
                pass

            try:
                # Attempt to extract the file size from the line and
                # update total file size
                file_size += int(data[-1])
            except Exception:
                pass

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                # calling printer
                printer(stat_count, file_size)

        # Print final statistics
        printer(stat_count, file_size)

    except KeyboardInterrupt:
        # Handle keyboard interruption (Ctrl+C) and print final statistics
        printer(stat_count, file_size)
        raise


if __name__ == '__main__':
    """ Import control """
    function()
