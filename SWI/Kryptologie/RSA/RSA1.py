import random


## @brief This function checks if a number is prime using the Miller-Rabin primality test.
#  @param n The number to be tested.
#  @param k The accuracy of the test.
#  @return 0 if the number is not prime, 1 if it is prime.
def is_prime_miller_rabin(n, k):
	assert n > 3
	if n%2 == 0:
		return 0

	r = 0
	n_test = n-1
	while True:
		if n_test%2 == 0:
			n_test //= 2
			r += 1
		else:
			d = n_test
			break

	for _ in range(k):
		is_continue = False
		a = random.randint(2, n-2)
		x = pow(a, d, n)

		if x == 1 or x == n-1:
			continue

		for _ in range(r-1):
			x = (x ** 2) % n
			if x == n-1:
				is_continue = True
				break

		if is_continue:
			continue
		return 0
	return 1



## @brief This function implements the Extended Euclidean Algorithm.
#  @param r1 The first number for the algorithm.
#  @param r2 The second number for the algorithm.
#  @param s1 The coefficient of r1 in the linear combination (default is 1).
#  @param s2 The coefficient of r2 in the linear combination (default is 0).
#  @param t1 The coefficient of r1 in the linear combination (default is 0).
#  @param t2 The coefficient of r2 in the linear combination (default is 1).
#  @return The greatest common divisor of r1 and r2, and the coefficients s and t.
def extended_ea(r1, r2, s1=1, s2=0, t1=0, t2=1):
    # Base case: if r2 is 0, return r1 and the coefficients s1 and t1
    if r2 == 0:
        # If s1 or t1 is negative, add s2 or t2 respectively
        if s1 < 0:
            s1 += s2
        if t1 < 0:
            t1 += t2
        return r1, s1, t1
    # Calculate the quotient and remainder of r1 and r2
    q, r = r1//r2, r1%r2
    # Calculate the new coefficients s and t
    s, t = s1-s2*q, t1-t2*q
    # Recursive call with r2, r, s2, s, t2, t
    return extended_ea(r2, r, s2, s, t2, t)


def generate_p_and_q(N):
	primes = []
	while True:
		candidate = random.randint(10**(N-1), 10**(N))
		is_prime = is_prime_miller_rabin(candidate, 10)
		if is_prime:
			primes.append(candidate)
		if len(primes) >= 2:
			break
	return primes


def generate_e(phi):
	while True:
		candidate = random.randint(2, phi)
		gcd, s, _ = extended_ea(candidate, phi)

		if gcd == 1:
			return candidate, s


def generate_keys(max_len=64):
    p, q = generate_p_and_q(max_len)
    n = p * q
    phi = (p-1) * (q-1)
    e, d = generate_e(phi)
    return p, q, phi, n, e, d


def check_e(e, phi):
    if 1 < e < phi:
        return True
    return False


def check_d(d, e, phi):
    if (e*d)%phi == 1:
        return True
    return False


def tASCII(message):
    ascii_table = []
    for i in message:
        ascii_table.append(ord(i))
    return ascii_table


def tBIN(message):
    bin_table = []
    for i in message:
        bin_table.append(bin(ord(i))[2:].zfill(8))
    return bin_table


def tNUM4(message):
    number_every_four = []
    big_bin = ""
    for i in message:
        big_bin += bin(ord(i))[2:].zfill(8)
    if len(big_bin) % 32 != 0:
        big_bin += "0" * (32 - (len(big_bin) % 32))
    for i in range(0, len(big_bin), 32):
        number_every_four.append(int(big_bin[i:i+32], 2))
    return number_every_four


def encryptNUM(NUMmessage, n, e):
    encrypted = []
    for i in NUMmessage:
        encrypted.append(pow(int(i), e, n))
    return encrypted


def decryptNUM(encrypted, n, d):
    decrypted = []
    for i in encrypted:
        decrypted.append(pow(i, d, n))
    return decrypted


def deNUMtoBIN(NUMmessage):
    bin_table = []
    for i in NUMmessage:
        bin_table.append(bin(i)[2:].zfill(32))
    return bin_table


def deBINtoASCII(BINmessage):
    ascii_table = []
    for i in BINmessage:
        while i.endswith('00000000'):  # Check if last 8 characters are '0'
            i = i[:-8]  # Remove last 8 characters
        for j in range(0, len(i), 8):
            ascii_table.append(chr(int(i[j:j+8], 2)))
    return ascii_table


def encryptFINAL(message, n, e):
    return encryptNUM(tNUM4(message), n, e)


def decryptFINAL(encrypted, n, d):
    decrypted = deBINtoASCII(deNUMtoBIN(decryptNUM(encrypted, n, d)))
    return "".join(decrypted)


def list_to_string(list):
    string = ""
    for i in list:
        
        string += str(i) + " "
    return string

        
def string_to_list(string):
    list = []
    for i in string.split(" "):
        if i != "":
            list.append(int(i))
    return list


def gen_table(message):
    table = []
    table.append(tASCII(message))
    table.append(tBIN(message))
    table.append(tNUM4(message))
    return table


if __name__ == '__main__':
    message = '0'
    max_len = 10
    print(gen_table(message))
    keys = generate_keys(max_len)
    print(keys)
    eFINAL = encryptFINAL(message, keys[3], keys[4])
    print(eFINAL)
    dFINAL = decryptFINAL(eFINAL, keys[3], keys[5])
    print(dFINAL)

