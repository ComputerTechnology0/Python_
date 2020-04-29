import string
import random

def password_generator(size = 8, chars = string.ascii_letters + string.digits + string.punctuation):
    
    return ''.join(random.choice(chars) for _ in range(size))

print(password_generator(int(input('How many characters in your password? '))))
