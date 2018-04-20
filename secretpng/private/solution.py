import zlib

BPP = 4         # bytes per pixel (RGB + A)
WIDTH = 484     # image width

# idat chunk data
idat = zlib.decompress(open("idat.bin", "rb").read())

data = ""

pos = 0
length = 0
byte = 0

while True:
    if pos == len(idat):
        break
    
    filter = idat[pos]
    
    byte = byte * 4 + filter
    length += 1
    
    if length == 4:
        data += chr(byte)
        byte = 0
        length = 0
    
    pos += BPP * WIDTH + 1  # skip line
print(data)