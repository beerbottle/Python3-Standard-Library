"""
Scan through string looking for the first location where the regular
expression pattern produces a match, and return a corresponding match object.
"""

import re


m = re.search('(?<=abc)def', 'abcdef')
out = m.group(0)
print(out)


m = re.search('(?<=-)\w+', 'spam-egg')
out = m.group(0)
print(out)
