def gen_primes():

	primes = []
	for i in range(2,1000):
		prime = True
		for j in range(2,i):
			if (i%j == 0):
				prime = False
		if prime:
			primes.append(i)
	return primes

