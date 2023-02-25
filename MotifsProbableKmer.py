# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
import random


def Motifs(Profile, Dna):
    Motifs=[]
    k=len(Profile[0])
    n=len(Dna[0])
    for i in range(n):
         Motifs.append(ProfileMostProbableKmer(Dna[i],k,Profile))
    return Motifs

# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.
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

def Pr(Text, profile):
    pro=1
    for i in range(len(Text)):
         pro = pro*profile[Text[i]][i]
    return pro 

Dna="TTACCTTAAC","GATGTCTGTC","ACGGCGTTAG","CCCTAACGAG","CGTCAGAGGT"

