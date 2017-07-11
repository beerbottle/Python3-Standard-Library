"""
difflib examples
"""
import difflib
from pprint import pprint
import sys


text1 = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
""".splitlines(keepends=True)
print(text1)
print(len(text1))
assert text1[0][-1] == '\n'


text2 = """
Beautiful is better than ugly.
Simple is better than complex.
Complex is better than complicated.
Sparse is better than dense.
Readability counts.
"""
d = difflib.Differ()
result = list(d.compare(text1, text2))
pprint(result)
print('-' * 50)
sys.stdout.writelines(result)
