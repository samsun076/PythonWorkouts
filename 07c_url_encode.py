"""Solution to chapter 2, exercise 7, beyond 3: URL-encoding"""

import string


#BOOK SOLUTION

def url_encode(text):
    """Given a string, replace any character that
    isn't a letter or number with % and its two-digit
    hex code.
    """

    safe_chars = string.ascii_letters + string.digits
    output = []
    for char in text:
        if char in safe_chars:
            output.append(char)
        else:
            output.append(hex(ord(char)).replace('0x','%'))
    return ''.join(output)

print(url_encode('David/'))
print(url_encode('https://you-are-right.com'))
