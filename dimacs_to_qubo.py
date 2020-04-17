import dwavebinarycsp
import dimod
import glob
from pathlib import Path

DIMACS_DIRECTORY = "instances/karatsuba/"
QUBO_DIRECTORY = "instances/karatsuba_qubo/"

def getQUBOfromDIMACS(path):
	with open(path, 'r') as fp:
		try:
			csp = dwavebinarycsp.cnf.load_cnf(fp)
		except ValueError:
			return None

	bqm = dwavebinarycsp.stitch(csp)
	return bqm.to_qubo()

def saveQUBO(path, qubo):
	file = open(path, "w")
	file.write(str(qubo))
	file.close()

def translateFiles(in_dir, out_dir):
	files = glob.glob(in_dir + "*.dimacs")

	for f in files:
		q = getQUBOfromDIMACS(f)
		if q != None:
			out_path = out_dir + Path(f).name.split(".")[0]+".qubo"
			saveQUBO(out_path, q)
		else:
			print("Processing " + f + " failed")
		

translateFiles(DIMACS_DIRECTORY, QUBO_DIRECTORY)