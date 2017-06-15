"""
SequenceMatcher object
"""

from difflib import SequenceMatcher


s = SequenceMatcher(None, " abcd", "abcd abcd")
out = s.find_longest_match(0, 5, 0, 9)
print(out)


s = SequenceMatcher(lambda x: x == " ", " abcd", "abcd abcd")
out = s.find_longest_match(0, 5, 0, 9)
print(out)


s = SequenceMatcher(None, "abxcd", "abcd")
out = s.get_matching_blocks()
print(out)


a = "qabxcd"
b = "abycdf"
s = SequenceMatcher(None, a, b)
for tag, i1, i2, j1, j2 in s.get_opcodes():
    print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
        tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))


s = SequenceMatcher(None, "abcd", "bcde")
print(s.ratio())
print(s.quick_ratio())
print(s.real_quick_ratio())


s = SequenceMatcher(lambda x: x == " ",
                    "private Thread currentThread;",
                    "private volatile Thread currentThread;")
print(round(s.ratio(), 3))


for block in s.get_matching_blocks():
    print("a[%d] and b[%d] match for %d elements" % block)


print('-' * 50)
for opcode in s.get_opcodes():
    print("%6s a[%d:%d] b[%d:%d]" % opcode)
