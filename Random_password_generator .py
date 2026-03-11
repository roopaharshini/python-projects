import random, string

chars = string.ascii_letters
password = ''.join(random.choice(chars) for _ in range(8))
print("Generated password:", password)

OUTPUT:
Generated password: dSZ
