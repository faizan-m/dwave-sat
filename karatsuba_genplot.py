import glob
import matplotlib
import matplotlib.pyplot as plt

INSTANCES_DIRECTORY = "instances/karatsuba/"
RESULTS_DIRECTORY = "results/karatsuba_complexity/"

def extractData():
	data = []

	files = glob.glob(INSTANCES_DIRECTORY + "*.dimacs")
	for f in files:
		d = {}

		fp = open(f)
		lines = fp.readlines()
		fp.close()

		d["variables"] = int(lines[0].split(" ")[2])
		d["clauses"] = int(lines[0].split(" ")[3])
		d["number"] = int(lines[2].split(" ")[3])
		d["factor1"] = int(lines[3].split(" ")[2])
		d["factor2"] = int(lines[3].split(" ")[4])

		data.append(d)

	return data

def genVarNum(data):
	v = []
	n = []

	for d in data:
		v.append(d["variables"])
		n.append(d["number"])

	fig, ax = plt.subplots()
	ax.scatter(n, v)
	ax.set(xlabel="Number", ylabel="Variables Used")
	fig.savefig(RESULTS_DIRECTORY+"VarNum.png")

def genClaNum(data):
	v = []
	n = []

	for d in data:
		v.append(d["clauses"])
		n.append(d["number"])

	fig, ax = plt.subplots()
	ax.scatter(n, v)
	ax.set(xlabel="Number", ylabel="Clauses Used")
	fig.savefig(RESULTS_DIRECTORY+"ClaNum.png")


def generatePlots():
	data = extractData()
	plots = [genVarNum, genClaNum]

	for p in plots:
		p(data)

generatePlots()