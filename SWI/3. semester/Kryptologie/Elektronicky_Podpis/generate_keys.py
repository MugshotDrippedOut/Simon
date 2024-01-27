import random
import os
import base64

# The Miller-Rabin primality test
# This function returns 1 if n is probably prime, and 0 if n is composite
# k is an input parameter that determines accuracy level
# The greater the value of k, the higher the accuracy
# An optimal value of k is k = ln(n) * 2^t, where t is the number of
#   Miller-Rabin tests performed
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


def generate_e(euler):
	while True:
		candidate = random.randint(2, euler)
		gcd, s, _ = extended_ea(candidate, euler)

		if gcd == 1:
			return candidate, s

def generate_keys(max_len=10):
    p, q = generate_p_and_q(max_len)
    n = p * q
    euler = (p-1) * (q-1)
    e, d = generate_e(euler)
    n = base64.b64encode(bytes(str(n), 'utf-8')).decode()
    e = base64.b64encode(bytes(str(e), 'utf-8')).decode()
    d = base64.b64encode(bytes(str(d), 'utf-8')).decode()
    return n, e, d

def keys_to_file():
    if not os.path.exists("folder\Private_key"):
        os.mkdir("folder\Private_key")
    if not os.path.exists("folder\Public_key"):
        os.mkdir("folder\Public_key")
    n, e, d = generate_keys()
    with open("folder\Private_key\Private_key.txt", "w") as f:
        f.write("{}".format(d))
        f.write("\n")
        f.write("{}".format(n))
    with open("folder\Public_key\Public_key.txt", "w") as f:
        f.write("{}".format(e))
        f.write("\n")
        f.write("{}".format(n))





if __name__ == "__main__":
    n, e, d = generate_keys()
    print("Public key: (n, e) = ({}, {})".format(n, e))
    print("Private key: (n, d) = ({}, {})".format(n, d))
    keys_to_file()