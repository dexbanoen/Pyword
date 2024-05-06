import random # random library
import string # string library

def generate_pw(length: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation # concat all uppercase, lowercase, digits and various punctuation characters
    password = ''.join(random.choice(alphabet) for i in range(length)) # joining random characters from above into password
    return password

testing = generate_pw() #testing
print(f"Generate password: {testing}") #print