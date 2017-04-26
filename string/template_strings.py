"""
Here is an example of how to use a Template
"""

from string import Template


s1 = Template('$who likes $what')
print(s1.substitute(who='tim', what='kung pao'))


s2 = Template('Give $who $100')
d = dict(who='tim')
print(s2.safe_substitute(d))

print(s1.safe_substitute(d))
