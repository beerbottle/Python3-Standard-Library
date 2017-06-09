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


text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""
entries = re.split('\n+', text)
print(entries)

out = [re.split(':?', entry, 3) for entry in entries]
print(out)

out = [re.split(':?', entry, 4) for entry in entries]
print(out)
