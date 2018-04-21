table = str.maketrans("qwertyuiopasdfghjklzxcvbnm", "😀😃😄😁😆😅😂😉🙃🙂😇😊🤣😌😍😘😗😙😚😋😎🤓🤗🤑🤒👿")

text = '''in cryptography, a substitution cipher is a method of encrypting by which units of plaintext are replaced with ciphertext, according to a fixed system; the "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth. the receiver deciphers the text by performing the inverse substitution.

substitution ciphers can be compared with transposition ciphers. in a transposition cipher, the units of the plaintext are rearranged in a different and usually quite complex order, but the units themselves are left unchanged. by contrast, in a substitution cipher, the units of the plaintext are retained in the same sequence in the ciphertext, but the units themselves are altered.

there are a number of different types of substitution cipher. if the cipher operates on single letters, it is termed a simple substitution cipher; a cipher that operates on larger groups of letters is termed polygraphic. a monoalphabetic cipher uses fixed substitution over the entire message, whereas a polyalphabetic cipher uses a number of substitutions at different positions in the message, where a unit from the plaintext is mapped to one of several possibilities in the ciphertext and vice versa.

a ctf cipher is a cipher where flag is hidden, for example ugractf substitutions are pretty easy. insert underscores between words and then submit the flag.'''.translate(table)

f = open("../public/message.txt", "w", encoding="utf-8")
print(text, file=f)
