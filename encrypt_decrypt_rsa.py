import rsa
import hashlib
import secrets
import string
import random
from random import getrandbits


publicKey, privateKey = rsa.newkeys(1024)
publicKey2, privateKey2 = rsa.newkeys(1024)

message = 'encrypted message'
password = 'SuperSafePassword'

e_message = rsa.encrypt(message.encode(), publicKey)
d_message = rsa.decrypt(e_message, privateKey).decode()

e_password = rsa.encrypt(password.encode(), publicKey2)
d_password = rsa.decrypt(e_password, privateKey2).decode()

h_password = hashlib.sha256(d_password.encode('utf-8')).hexdigest()
password = hashlib.sha256(password.encode('utf-8')).hexdigest()

print(f'Encrypted password: {e_message}')
print(f'Decrypted password: {d_message}')

print(f'Encrypted: {e_password}')
print(f'Decrypted: {d_password}')
print(f'Hashed password: {h_password}')

key = secrets.token_urlsafe(24)
print('Random token:', key)

# random string generator 32 for 256 bits key
rand_string = ''.join(random.sample(string.ascii_letters, 32))
print('Random string:', rand_string)

randValue = ''.join(map(str, [secrets.randbits(16) for i in range(4)]))
print(randValue)

value = getrandbits(192)
print(value)




