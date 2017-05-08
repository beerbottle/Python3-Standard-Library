"""
Return the string obtained by replacing the leftmost non-overlapping
occurrences of pattern in string by the replacement repl.
"""

import re


out = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
             r'static PyObject*\npy_\1(void)\n{',
             'def myfunc():')
print(out)
