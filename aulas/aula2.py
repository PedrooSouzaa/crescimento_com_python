# \r\n - quebra de linha -> CRLF

print(12, 34, 1001, sep='-')
print(56, 78, sep="-")

print(12, 34, sep='')
print(56, 78, sep="##")

print(56, 78, end='\r\n')
print(56, 78, end='\n')