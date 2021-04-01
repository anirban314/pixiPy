import os
import math

def getpixels(limit):
	cpath = 'cache/primes.txt'

	#Execute this if cache file EXISTS
	if os.path.isfile(cpath):
		print("Cache file found: Reading primes from cache...")
		primes = readfile(limit, cpath)

		#Execute this if required no. of primes EXISTS in cache file
		if len(primes) == limit:
			return primes
		
		#Execute this if required no. of primes DOES NOT exist in cache file
		else:
			print("Reached EOF: Generating missing primes...")
			new_limit = limit - len(primes)
			last_prime = primes[-1]
			new_primes = getprimes(new_limit, last_prime)
			primes.extend(new_primes)

			print("Appending generated primes to cache file...")
			writefile(new_primes, cpath, mode='a')
			return primes
	
	#Execute this if cache file DOES NOT exist
	else:
		print("Cache file missing: Generating primes...")
		primes = getprimes(limit)

		print("Writing generated primes to new cache file...")
		writefile(primes, cpath)

		return primes


def readfile(limit, cpath):
	primes = []
	with open(cpath, 'r') as file:
		while len(primes) < limit:
			prime = file.readline().strip()
			if not prime:
				break
			primes.append(int(prime))
	return primes


def writefile(primes, cpath, mode='w'):
	sprimes = [f"{prime}\n" for prime in primes]
	with open(cpath, mode) as file:
		file.writelines(sprimes)


def getprimes(limit, start=1):
	primes = [2] if start==1 else []
	number = start + 2
	
	while len(primes) < limit:
		if isprime(number):
			primes.append(number)
		number += 2
	return primes


def isprime(number):
	for d in range(3, int(math.sqrt(number))+1, 2):
		if number % d == 0:
			return False
	return True


if __name__ == '__main__':
	getpixels(int(input('Standalone Mode - Enter number of primes to generate: ')))


'''
take care of the missing folder bug
'''