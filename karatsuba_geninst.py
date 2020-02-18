import requests

API_ENDPOINT = "https://toughsat.appspot.com/generate"
SAVE_DIRECTORY = "instances/karatsuba/"
FILE_SUFFIX = ".dimacs"
PRIMES = [2, 3, 5, 7, 9, 11, 13, 17]

def generateToughSat(f1, f2):
	params = {"type": "factoring2017", "includefactors": "on", "factor1": f1, "factor2": f2}
	r = requests.post(API_ENDPOINT, params)
	return r.text

def saveDimacs(data, location):
	file = open(location, "w")
	file.write(data)
	file.close()

def generateInstances(ps):
	for i, p1 in enumerate(ps):
		for p2 in ps[i:len(ps)]:
			sat = generateToughSat(p1, p2)
			saveDimacs(sat, SAVE_DIRECTORY+str(p1*p2)+FILE_SUFFIX)
			print("Saved SemiPrime" + str(p1) + "x" + str(p2) + "=" + str(p1*p2))


generateInstances(PRIMES)