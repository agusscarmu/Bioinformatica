def GreedySearch(dna,k,t):
    BestMotif=[]
    n=len(dna[0])
    for i in range(0,t):
        BestMotif.append(dna[i][0:0+k])
    for i in range(n-k+1):
        Motif=[]
        Motif.append(dna[0][i:i+k])
        for j in range(1, t):
            p=CountWithPseudocounts(Motif[0:j])
            Motif.append(ProfileMostProbableKmer(dna[j],k,p))
        if Score(Motif)>Score(BestMotif):
            BestMotif=Motif
        
    return BestMotif

def Consensus(Motifs):
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    consensus=""
    for j in range(k):
        m=0
        frequentSymbol=""
        for symbol in "ACGT":
              if count[symbol][j]>m:
                   m=count[symbol][j]
                   frequentSymbol=symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    consensus = Consensus(Motifs)
    count = 0
    k = len(Motifs[0])
    for Motif in Motifs:
         for i in range(k):
            if Motif!=consensus[i]:
                count+=1
    return count

def ProfileMostProbableKmer(dna,k,p):
    MayorProb=0
    MasProb=dna[:k]
    n=len(dna)
    for i in range(n-k+1):
        pattern=dna[i:i+k]
        pr=Pr(dna,p)
        if(pr>MayorProb):
            MayorProb=pr
            MasProb=pattern
    
    return MasProb

def Pr(Text, profile):
    pro=1
    for i in range(len(Text)):
         pro = pro*profile[Text[i]][i]
    return pro 

def CountWithPseudocounts(Motifs):
    t=len(Motifs)
    k=len(Motifs[0])
    count={}
    for symbol in "ACGT":
        count[symbol]=[]
        for j in range(k):
            count[symbol].append(1)
    for j in range(t):
        for i in range(k):
            count[Motifs[j][i]][i]+=1
    return count

# def Count(Motif):
#     count={}
#     k=len(Motif[0])
#     for symbol in "ACGT":
#         count[symbol]=[]
#         for j in range(k):
#             count[symbol].append(0)
#     t=len(Motif)
#     for i in range(t):
#         for j in range(k):
#             symbol=Motif[i][j]
#             count[symbol][j]+=1

#     for symbol in "ACGT":
#         for i in range(k):
#             count[symbol][i]/=t
    
#     return count


profile = {

    'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
    'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
    'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
    'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}
dna=["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"]
k=3
t=5
print(GreedySearch(dna,k,t))
