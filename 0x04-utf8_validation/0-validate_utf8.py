#!/usr/bin/python3

"""
Mission V: Write a method that determines if a given
 data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ UTF-8 validator """
    # Variable to track the number of trailing bytes
    # needed for the current character
    trailing_bytes = 0

    # Iterate through each integer in the data
    for num in data:
        # Extract the least significant 8 bits
        # of the integer (equivalent to a byte)
        byte = num & 0xFF

        # If trailing_bytes is not zero, we are
        # in the middle of a multi-byte character
        if trailing_bytes:
            # Check if the current byte is a valid trailing byte
            if byte >> 6 != 2:
                return False
            trailing_bytes -= 1
            continue

        # Determine the number of leading 1 bits to identify
        # the start of a multi-byte character
        while (1 << (7 - trailing_bytes)) & byte:
            trailing_bytes += 1

        # Validate the number of leading 1 bits and trailing bytes
        if trailing_bytes == 1 or trailing_bytes > 4:
            return False

        # Adjust trailing_bytes for the next iteration
        trailing_bytes = max(trailing_bytes - 1, 0)

    # Check if there are no incomplete characters at the end of the data
    return trailing_bytes == 0
