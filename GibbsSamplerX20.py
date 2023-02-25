import random

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            break
        
    return BestMotifs

def Pr(Text, profile):
    pro=1
    for i in range(len(Text)):
         pro = pro*profile[Text[i]][i]
    return pro 

def ProfileMostProbableKmer(text, k, profile):
    Mayorprob = 0
    MasProb = text[:k]
    n=len(text)
    for i in range(n-k+1):
         FragText=text[i:i+k]
         prob = Pr(FragText, profile)
         if(prob>Mayorprob):
              Mayorprob=prob
              MasProb=FragText
    return MasProb

def Motifs(Profile, Dna):
    Motifs=[]
    k=len(Profile["A"])
    t=len(Dna)
    for j in range(t):
        Motifs.append(ProfileMostProbableKmer(Dna[j],k,Profile))
    return Motifs

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
            if Motif[i]!=consensus[i]:
                count+=1
    return count

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


def ProfileWithPseudocounts(Motifs):
    profile = CountWithPseudocounts(Motifs)
    for i in range(len(Motifs[0])):
        num=0 
        for symbol in "ACGT":
            num = num + profile[symbol][i]
        for symbol in "ACGT":
            profile[symbol][i]/=num
    return profile

def RandomMotifs(Dna, k, t):
    x=len(Dna[0])
    Motif=[]
    for i in range(t):
        randomIndex=random.randint(0,(x-k))
        Motif.append(Dna[i][randomIndex:randomIndex+k])
    return Motif


def GibbsSampler(Dna, k, t, N):
    BestMotifs = RandomizedMotifSearch(Dna, k, t)
    for _ in range(N):
        Motif=RandomizedMotifSearch(Dna,k,t)
        if Score(Motif)<Score(BestMotifs):
            BestMotifs=Motif
    return BestMotifs
# Copy the ten strings occurring in the hyperlinked DosR dataset below.
Dna =["GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC", "CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG", "ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC", "GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC", "GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG", "CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA", "GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA", "GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG", "GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG", "TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"]

# set t equal to the number of strings in Dna, k equal to 15, and N equal to 100
t=len(Dna)
k=15
N=100
# Call GibbsSampler(Dna, k, t, N) 20 times and store the best output in a variable called BestMotifs
def RepeatedGibbsSampler(Dna, k, t, N):
    BestMotif=GibbsSampler(Dna, k, t, N)
    for _ in range(20):
        Motif=GibbsSampler(Dna, k, t, N)
        if Score(Motif)<Score(BestMotif):
            BestMotif=Motif
    return BestMotif
# Print the BestMotifs variable
BestMotifs=RepeatedGibbsSampler(Dna, k, t, N)
print(BestMotifs)
# Print Score(BestMotifs)
print(Score(BestMotifs))