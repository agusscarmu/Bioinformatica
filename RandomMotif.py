import random


def RandomMotifs(Dna, k, t):
    x=len(Dna[0])
    Motif=[]
    for i in range(t):
        randomIndex=random.randint(0,(x-k))
        Motif.append(Dna[i][randomIndex:randomIndex+k])
    return Motif

Dna="TTACCTTAAC","GATGTCTGTC","ACGGCGTTAG","CCCTAACGAG","CGTCAGAGGT"

t=len(Dna)
k=3
Motifs=RandomMotifs(Dna,k,t)
print(Motifs)