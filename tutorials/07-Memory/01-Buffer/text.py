import binascii
def split_every(n, s):
    return [ s[i:i+n] for i in xrange(0, len(s), n) ]

filename = 'text.dat'
with open(filename, 'rb') as f:
    content = f.read()

list = split_every(2, binascii.hexlify(content))
for i in list:
    if i != "0a":
        print(i)
