import re

formats = ['%s.','SECTION %s','§ %s.']

level = ['_','_','_']

index = formats[2] % level[2]
print(index)

expression = '^\\((\\d+[a-z]*)\\)\\s+(.*)$'
para = '(1)  1. Income from non-self-employed work includes salaries, wages, bonuses, profit-sharing, and other benefits and advantages for employment in the public or private sector;'

m = re.match(expression, para)
s1 = m.group(1)
print(s1)

x = '%sHi' % '_'
print(x)