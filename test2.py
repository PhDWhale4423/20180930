a = bytes('abc\0', 'ASCII')
print("a = ", a)
print("a = ", repr(a))
print()

if a[-1] == bytes('\0', 'ASCII'):
    print('True')
else:
    print('False')

print()

print("bytes('\\0', 'ASCII') = ", bytes('\0', 'ASCII'))
print("bytes('\\0', 'ASCII') = ", repr(bytes('\0', 'ASCII')))
print(type(bytes('\0', 'ASCII')))
print()
print('a[-1] = ', a[-1])
print('a[-1] = ', repr(a[-1]))
print(type(a[-1]))

print()
print('なﾞんﾞてﾞたﾞよﾞ！')

print()
if a[-1] == 0x00:
    print('これが正攻法?')
