import dwavebinarycsp
import dimod

with open("nums/6.dimacs", 'r') as fp: # doctest: +SKIP
	csp = dwavebinarycsp.cnf.load_cnf(fp)

#csp = dwavebinarycsp.factories.random_2in4sat(8, 4)  # 8 variables, 4 clauses

bqm = dwavebinarycsp.stitch(csp)

resp = dimod.SimulatedAnnealingSampler().sample(bqm)

for sample, energy in resp.data(['sample', 'energy']):
    print(sample, csp.check(sample), energy)