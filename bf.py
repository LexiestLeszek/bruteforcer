from time import time
from itertools import product
import string

def product_loop(password, generator):
    for p in generator:
        if ''.join(p) == password:
            print('\nPassword:', ''.join(p))
            return ''.join(p)
    return False

def load_password_set(filename):
    with open(filename, 'r') as file:
        return set(line.strip() for line in file)

def bruteforce(password):
    
    print('1. Comparing with most common passwords dictionary')
    common_pass_set = load_password_set('dict_attack.txt')
    user_specific_set = load_password_set('user_spec_passwords.txt')

    if password in user_specific_set:
        print('\nPassword:', password)
        return password

    if password in common_pass_set:
        print('\nPassword:', password)
        return password

if __name__ == "__main__":
    begin = time()
    bruteforce("Qwerty123")
    finish = time()
    print('Time spent to solve: %.2f secs' % (finish - begin))
    
