import zlib
import binascii

BPP = 4         # bytes per pixel
WIDTH = 484     # width of image

# idat.bin — IDAT chunk contents
contents = zlib.decompress(open("idat.bin", "rb").read())

raw_result = bytearray()

encstr = '''It was really hard to solve, but you got here now! Congratulations!
Hope you'll find useful such advanced knowledge of PNG file structure.
Now it's time to solve next tasks, so flag is ugractfeveryonelikespngfilters.'''

pos = 0

_data = bytearray([0]*(WIDTH*BPP))

def safe_mod(x):
    return (x % 256 + 256) % 256

dp = 0
while True:
    if len(contents) == dp:
        break
    
    filter = contents[dp]
    dp += 1
    
    if filter != 0:
        print("Strange: FILTER NOT 0!", filter, dp)
    data = contents[dp:dp+WIDTH*BPP]
    dp += WIDTH*BPP
    
    filter = ((ord(encstr[pos // 4]) >> ((3 - pos % 4) * 2))) & 0b11
    raw_result += bytearray([filter])
    
    new_data = bytearray([0]*(WIDTH*BPP))
    
    for i in range(WIDTH*BPP):
        if filter == 0:
            # None filter
            new_data[i] = data[i]
        elif filter == 1:
            # Sub filter
            if i < BPP:
                old = 0
            else:
                old = data[i - BPP]
            new_data[i] = safe_mod(data[i] - old)
        elif filter == 2:
            # Up filter
            new_data[i] = safe_mod(data[i] - _data[i])
        elif filter == 3:
            # Average filter
            if i < BPP:
                raw_bpp = 0
            else:
                raw_bpp = data[i - BPP]
            prior = _data[i]
            new_data[i] = safe_mod(data[i] - (raw_bpp + prior) // 2)
    
    raw_result += new_data
    pos += 1
    
    _data = data

# writing full IDAT chunk (not only chunk data, but length, type and CRC) 
comp = zlib.compress(raw_result, level=9)
f = open("idat_modified.bin", "wb")
f.write(len(comp).to_bytes(4, "big"))
f.write(b"IDAT")
f.write(comp)
f.write(zlib.crc32(b"IDAT"+comp).to_bytes(4, "big"))
f.close()
