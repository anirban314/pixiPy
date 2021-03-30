import os
import math

def getpixels(limit):
	cpath = 'cache/primes.txt'

	#Execute this if cache file EXISTS
	if os.path.isfile(cpath):
		print("Cache file found: Reading primes from cache...", end=' ')
		primes = readfile(limit, cpath)

		#Execute this if required no. of primes EXISTS in cache file
		if len(primes) == limit:
			print("[Success]")
			return primes
		
		#Execute this if required no. of primes DOES NOT exist in cache file
		else:
			print("[FAILED]\nReached EOF: Generating missing primes...", end=' ')
			missing = limit - len(primes)
			last = primes[-1]
			new_primes = getprimes(missing, last)
			primes.extend(new_primes)

			print("[Success]\nAppending generated primes to cache file...", end=' ')
			writefile(new_primes, cpath, mode='a')
			
			print("[Success]")
			return primes
	
	#Execute this if cache file DOES NOT exist
	else:
		print("Cache file missing: Generating primes...", end=' ')
		primes = getprimes(limit)

		print("[Success]\nWriting generated primes to new cache file...", end=' ')
		writefile(primes, cpath)

		print("[Success]")
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


def getprimes(limit, last=1):
	primes = [2] if last==1 else []
	number = last + 2
	
	while len(primes) < limit:
		if isprime(number):
			primes.append(number)
		number += 2
	return primes


def isprime(number):
	for d in range(3, int(math.sqrt(number))+1, 2):
		if number % d == 0 : return False
	return True


if __name__ == '__main__':
	print(len(getpixels(int(input('Standalone Mode - Enter number of primes to generate: ')))))


'''
take care of the missing folder bug
'''