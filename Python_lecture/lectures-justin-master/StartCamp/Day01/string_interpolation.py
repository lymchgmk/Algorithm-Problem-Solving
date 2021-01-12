#1. 가장 초창기
print('%s %s' % ('one', 'two'))
print('%i %s' % (1, 'two'))

#2. pyformat
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

#3. f-string
a, b = ('one', 'two')
print(f'{a} {b}')
print(f'{b} {a}')