genome = input()
genome = genome.lower()
qtygenome = len(genome)
Cnucl = genome.count('c')
Gnucl = genome.count('g')
GCnucl = (Cnucl + Gnucl) / qtygenome * 100
print(GCnucl)
