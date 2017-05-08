"""
Split string by the occurrences of pattern.
"""

import re


out = re.split('\W+', 'Words, words, words.')
print(out)


out = re.split('(\W+)', 'Words, words, words.')
print(out)


out = re.split('\W+', 'Words, words, words.', maxsplit=1)
print(out)


out = re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
print(out)


out = re.split('(\W+)', '...words, words...')
print(out)


# split() doesn’t currently split a string on an empty pattern match.
out = re.split('x*', 'axbc')
print(out)


try:
    out = re.split('^$', 'foo\n\nbar\n', flags=re.M)
    print(out)
except ValueError as e:
    print(e)
