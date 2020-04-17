import dwavebinarycsp
import dimod
import glob
from pathlib import Path
import multiprocessing
import time

DIMACS_DIRECTORY = "instances/karatsuba/"
QUBO_DIRECTORY = "instances/karatsuba_qubo/"
TIMEOUT = 5

def getTimedQUBOfromDIMACS(path, t):
	manager = multiprocessing.Manager()
	return_dict = manager.dict()
	p = multiprocessing.Process(target= getQUBOfromDIMACS, args=(path, return_dict))
	p.start()
	p.join(t)

	if p.is_alive():
		print("Processing " + path +  " timed out")
		p.terminate()
		p.join()
		return None

	return return_dict[0]

def getQUBOfromDIMACS(path, return_dict):
	with open(path, 'r') as fp:
		try:
			csp = dwavebinarycsp.cnf.load_cnf(fp)
		except ValueError:
			return_dict[0] = None
			return

	bqm = dwavebinarycsp.stitch(csp)

	return_dict[0] = bqm.to_qubo()

def saveQUBO(path, qubo):
	file = open(path, "w")
	file.write(str(qubo))
	file.close()

def translateFiles(in_dir, out_dir):
	files = glob.glob(in_dir + "*.dimacs")

	for f in files:
		q = getTimedQUBOfromDIMACS(f, TIMEOUT)
		if q != None:
			out_path = out_dir + Path(f).name.split(".")[0]+".qubo"
			saveQUBO(out_path, q)
		else:
			print("Processing " + f + " failed")
		

translateFiles(DIMACS_DIRECTORY, QUBO_DIRECTORY)