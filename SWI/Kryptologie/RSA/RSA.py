import random
import math
import sys
sys.set_int_max_str_digits(1000000)

def generate_prime(n):
    first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                         31, 37, 41, 43, 47, 53, 59, 61, 67,
                         71, 73, 79, 83, 89, 97, 101, 103,
                         107, 109, 113, 127, 131, 137, 139,
                         149, 151, 157, 163, 167, 173, 179,
                         181, 191, 193, 197, 199, 211, 223,
                         227, 229, 233, 239, 241, 251, 257,
                         263, 269, 271, 277, 281, 283, 293,
                         307, 311, 313, 317, 331, 337, 347, 349,
                         353, 359, 367, 373, 379, 383, 389, 397,
                         401, 409, 419, 421, 431, 433, 439, 443,
                         449, 457, 461, 463, 467, 479, 487, 491,
                         499, 503, 509, 521, 523, 541, 547, 557,
                         563, 569, 571, 577, 587, 593, 599, 601,
                         607, 613, 617, 619, 631, 641, 643, 647,
                         653, 659, 661, 673, 677, 683, 691, 701,
                         709, 719, 727, 733, 739, 743, 751, 757,
                         761, 769, 773, 787, 797, 809, 811, 821,
                         823, 827, 829, 839, 853, 857, 859, 863,
                         877, 881, 883, 887, 907, 911, 919, 929,
                         937, 941, 947, 953, 967, 971, 977, 983,
                         991, 997]

    # Function to generate a random number of n bits
    def nBitRandom(n):
        return random.randrange(2**(n-1)+1, 2**n - 1)

    # Function to get a low level prime number
    def getLowLevelPrime(n):
        while True:
            pc = nBitRandom(n)
            # Check divisibility of pc with first primes
            for divisor in first_primes_list:
                if pc % divisor == 0 and divisor**2 <= pc:
                    break
            else:
                return pc

    # Function to check if a number passes the Miller-Rabin primality test
    def isMillerRabinPassed(mrc):
        maxDivisionsByTwo = 0
        ec = mrc-1
        # Count the number of times ec is divisible by 2
        while ec % 2 == 0:
            ec >>= 1
            maxDivisionsByTwo += 1
        assert(2**maxDivisionsByTwo * ec == mrc-1)

        # Function to check if a number is a composite number
        def trialComposite(round_tester):
            if pow(round_tester, ec, mrc) == 1:
                return False
            for i in range(maxDivisionsByTwo):
                if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                    return False
            return True

        # Number of trials to perform in the Miller-Rabin test
        numberOfRabinTrials = 20
        for i in range(numberOfRabinTrials):
            round_tester = random.randrange(2, mrc)
            if trialComposite(round_tester):
                return False
        return True

    # Main loop to generate a prime number
    while True:
        possible_prime = getLowLevelPrime(n)
        # If the number passes the Miller-Rabin test, return it as a prime
        if not isMillerRabinPassed(possible_prime):
            continue
        else:
            return possible_prime

def random_prime(min_value, max_value):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    
    while True:
        prime = random.randint(min_value, max_value)
        if is_prime(prime):
            return prime

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(e, euler):
    g, x, _ = extended_gcd(e, euler)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % euler

def RSA_generate_keys(min_value, max_value):
    p = random_prime(min_value, max_value)
    q = random_prime(min_value, max_value)
    n = p * q
    euler = (p - 1) * (q - 1)
    e = random_prime(1, euler)
    while math.gcd(e, euler) != 1:
        e = random_prime(1, euler)
    d = mod_inverse(e, euler)
    return p, q, euler, n, e, d


def RSA_encrypt(message, n, e):
    encrypted = []
    for i in message:
        encrypted.append((ord(i)**e)%n)
    return encrypted

def RSA_decrypt(encrypted, n, d):
    decrypted = []
    for i in encrypted:
        decrypted.append(chr((i**d)%n))
    return decrypted


def message_to_bin(message):
    message_bin = ""
    for i in message:
        message_bin += bin(ord(i))[2:].zfill(8)
    return message_bin


def bin_to_dec(message_bin):
    message_dec = []
    for i in range(0, len(message_bin), 8):
        message_dec.append(int(message_bin[i:i+8], 2))
    return message_dec
    
    
def dec_to_ascii(message_dec):
    try:
        message_ascii = ""
        for i in message_dec:
            message_ascii += chr(i)
        return message_ascii
    except:
        return None
    
    
def bin_to_number(message_bin):
    return int(message_bin, 2)


def number_to_bin(message_number):
    bin_number = bin(message_number)[2:]
    number_of_zeros = 8 - len(bin_number)%8
    return "0"*number_of_zeros + bin_number



def printRSA(message, min_value, max_value):
    message_bin = message_to_bin(message)
    message_number = bin_to_number(message_bin)
    print("Message in binary: ", message_bin)
    print("Message in number: ", message_number)
    keys = RSA_generate_keys(min_value, max_value)
    print("p: ", keys[0])
    print("q: ", keys[1])
    print("euler: ", keys[2])
    print("n: ", keys[3])
    print("e: ", keys[4])
    print("d: ", keys[5])
    encrypted = RSA_encrypt(message, keys[3], keys[4])
    print("Encrypted: ", encrypted)
    decrypted = RSA_decrypt(encrypted, keys[3], keys[5])
    print("Decrypted: ", decrypted)
    
    

    

if __name__ == "__main__":
    message = "Hello World!"
    min_value = 10**2
    max_value = 10**4
    #printRSA(message, min_value, max_value)
    
    print(generate_prime(32))
    pass
    
    
    