import requests
import os.path

API_ENDPOINT = "https://toughsat.appspot.com/generate"
SAVE_DIRECTORY = "instances/karatsuba/"
FILE_SUFFIX = ".dimacs"
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

def existsToughSat(f1, f2):
	return os.path.isfile(SAVE_DIRECTORY + str(f1*f2)+".dimacs")

def checkNotHtml(text):
	return not "html" in text

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
			if(not existsToughSat(p1, p2)):
				sat = generateToughSat(p1, p2)
				if(checkNotHtml(sat)):
					saveDimacs(sat, SAVE_DIRECTORY+str(p1*p2)+FILE_SUFFIX)
					print("Saved SemiPrime" + str(p1) + "x" + str(p2) + "=" + str(p1*p2))
				else:
					print("Failed SemiPrime" + str(p1) + "x" + str(p2) + "=" + str(p1*p2))


generateInstances(PRIMES)