# y=b"python"
# print(y,type(y)) #b'python' bytes
# print(list(y))#[112, 121, 116, 104, 111, 110]
# print(tuple(y))#(112, 121, 116, 104, 111, 110)
# print(set(y))#{104, 110, 111, 112, 116, 121}

# y=b"python"
# for i in y:
    # print(i)#answer get ascii values in vertically
# y=b"python"
# for i in y:
    # print(i,end=" ")#112 121 116 104 111 110 

# print(ord('P'))#80
# print(chr(80))#P

# y=b"python"
# y[0]=80#TypeError: 'bytes' object does not support item assignment

# y=b'[1,2,3]'
# print(list(y))#[91, 49, 44, 50, 44, 51, 93]
# print(ord('['))#91
# print(ord(']'))#93
# print(ord(','))#44

# m=bytearray(b"python")
# print(m)#bytearray(b'python')
# print(m[0])#112
# print(ord('p'))#112
# m[0]=88
# print(m)#bytearray(b'Xython')
# print(ord('X'))#88


