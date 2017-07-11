"""string format examples"""

from datetime import datetime


s = '{0}, {1}, {2}'.format('a', 'b', 'c')
print(s)


s = '{}, {}, {}'.format('a', 'b', 'c')
print(s)


s = '{2}, {1}, {0}'.format('a', 'b', 'c')
print(s)


s = '{2}, {1}, {0}'.format(*'abc')
print(s)


s = '{0}, {1}, {0}'.format('hello', 'world')
print(s)


s = 'Coordinates: {latitude}, {longitude}'.format(
    latitude='37.24N', longitude='-115.81W')
print(s)


coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
s = 'Coordinates: {latitude}, {longitude}'.format(**coord)
print(s)


c = 3 - 5j
s = 'The complex number: {0}, real part: {0.real}, ' \
    'imaginary part: {0.imag}'.format(c)
print(s)


class Point:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f'Point({self.x}, {self.y})'


print(Point(4, 2))


coord = [3, 5]
s = 'X: {0[0]}, Y: {0[1]}'.format(coord)
print(s)


s = "repr() shows quotes: {!r}, str() doesn't: {!s}".format('test1', 'test2')
print(s)


print('{:<30}'.format('left aligned'))
print('{:>30}'.format('right aligned'))
print('{:^30}'.format('centered'))
print('{:*^30}'.format('centered'))


print('{:+f}, {:+f}'.format(3.14, 3.14))
print('{:f}, {:f}'.format(3.14, 3.14))
print('{:-f}, {:-f}'.format(3.14, 3.14))


print("int: {0:d}, hex: {0:x}, oct: {0:o}, bin: {0:b}".format(42))
print("int: {0:d}, hex: {0:#x}, oct: {0:#o}, bin: {0:#b}".format(42))


print('{:,}'.format(1234567890))


points = 19
total = 22
print('Correct anwsers: {:.2%}'.format(points / total))


print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))


for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill}{align}30}'.format(text, fill=align, align=align))


octets = [192, 168, 0, 1]
s = '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
print(s)
print(int(s, 16))


for num in range(5, 12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, width=5, base=base), end='')
    print()
