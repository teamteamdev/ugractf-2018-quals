plaintext = b"https://gist.githubusercontent.com/nsychev/6b25ae3c8a31e70adc440b977c78c8b4/raw/e9c3a9a77c9485fd255bf503fb03bebe5329832a/flag"

key = b"elonmusk"

data = b""
for i in range(len(plaintext)):
    data += bytearray([plaintext[i] ^ key[i % len(key)]])
print(data)