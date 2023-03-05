import primegen

def test_prime_generation():
	primes = primegen.gen_primes()
	assert primes[4] == 11
	assert primes[7] == 19
	assert primes[14] == 47
	assert primes[len(primes)-1] == 997
