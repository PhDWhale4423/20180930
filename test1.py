a = 'abc\0'
print("a = ", a)
print("a = ", repr(a))
print()

if a[-1] == '\0':
    print('True')
else:
    print('False')

print()

print('a[-1] = ', a[-1])
print('a[-1] = ', repr(a[-1]))
print(type(a[-1]))
print()
print("'\\0' = ", '\0')
print("'\\0' = ", repr('\0'))
print(type('\0'))

print()
print('なるほどな')
