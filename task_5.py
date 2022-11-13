from string import ascii_uppercase, ascii_lowercase, digits
from random import sample

def get_random_password(n=8) -> str:
    SYMBOLS = ascii_uppercase + ascii_lowercase + digits
    password = "".join(sample(SYMBOLS, n))
    return password

print(get_random_password())
print(get_random_password(5))
print(get_random_password(n=10))
