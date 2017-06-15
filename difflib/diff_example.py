"""
difflib examples
"""

import keyword
import sys
import difflib


s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
sys.stdout.writelines(difflib.context_diff(
    s1, s2, fromfile='before.py', tofile='after.py'))
print('-' * 50)
sys.stdout.writelines(difflib.unified_diff(
    s1, s2, fromfile='before.py', tofile='after.py'))


out = difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])
print(out)

out = difflib.get_close_matches('wheel', keyword.kwlist)
print(out)

out = difflib.get_close_matches('accept', keyword.kwlist)
print(out)
print('-' * 50)


diff = difflib.ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
                     'ore\ntree\nemu\n'.splitlines(keepends=True))
# print(''.join(diff), end='')
print('-' * 50)
# print(''.join(difflib.restore(list(diff), 1)), end='')
print(''.join(difflib.restore(list(diff), 2)), end='')
