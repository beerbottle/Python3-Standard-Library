"""
Return the string obtained by replacing the leftmost non-overlapping
occurrences of pattern in string by the replacement repl.
"""

import re
import string


out = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
             r'static PyObject*\npy_\1(void)\n{',
             'def myfunc():')
print(out)


def dashrepl(matchobj):
    if matchobj.group(0) == '-':
        return ' '
    else:
        return '-'


out = re.sub('-{1,2}', dashrepl, 'pro----gram-files')
print(out)

out = re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
print(out)

out = re.escape('python.exe')
print(out)

legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
print('[%s]+' % re.escape(legal_chars))

operators = ['+', '-', '*', '/', '**']
print('|'.join(map(re.escape, sorted(operators, reverse=True))))


pattern = re.compile('d')
out = pattern.search('dog')
print(out)
out = pattern.search('dog', 1)  # No match, search doesn't includethe "d".
print(out)


pattern = re.compile('o')
out = pattern.match('dog')  # No match as "o" is not at the start of "dog".
print(out)
out = pattern.match('dog', 1)  # # Match as "o" is the 2nd character of "dog".
print(out)


pattern = re.compile('o[gh]')
out = pattern.fullmatch('dog')  # No match as "o" is not at the start of "dog".
print(out)
out = pattern.fullmatch('ogre')  # No match as not the full string matches.
print(out)
out = pattern.fullmatch('doggie', 1, 3)  # Matches within given limits.
print(out)


m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(1, 2))
print(m[0])
print(m[1])
print(m[2])


m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.group('first_name'))
print(m.group('last_name'))
print(m.group(0))
print(m.group(1))
print(m.group(2))


m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
print(m.group(1))  # Returns only the last match.


m = re.match(r"(\d+)\.(\d+)", "24.1632")
print(m.groups())


m = re.match(r"(\d+)\.?(\d+)?", "24")
print(m.groups())
print(m.groups('0'))


m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.groupdict())


email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
out = email[:m.start()] + email[m.end():]
print(out)
