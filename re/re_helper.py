"""
In this example, we’ll use the following helper function to display match objects a little more gracefully.
"""

import re


def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())


valid = re.compile(r"^[a2-9tjqk]{5}$")
out = displaymatch(valid.match("akt5q"))
print(out)
