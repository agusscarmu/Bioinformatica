def PatternCount(Text, Pattern):
    count=0
    
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count=count+1

    return count

# Nos da un diccionario con la cantidad de frecuencia de un patron en un segmento de ADN
def FrequencyTable(Text, k):
    frequMap={}
    n=len(Text)
    for i in range(n-k):
        Pattern= Text[i:i+k]
        if Text[i:i+k] not in frequMap:     
            frequMap[Pattern]=1
        elif Pattern == Text[i:i+k]:
            frequMap[Pattern] += 1

    return frequMap

# Nos devuelve los patrones con mayor repeticion
def BetterFrequentWord(Text,k):
    FrequentPattern=[]
    freqMap=FrequencyTable(Text,k)
    max=MaxMap(freqMap)
    for Pattern in freqMap:
        if freqMap[Pattern] == max:
            FrequentPattern.append(Pattern)
    return FrequentPattern

def MaxMap(freqMap):
    mayor=0
    for Pattern in freqMap:
        if freqMap[Pattern]>mayor:
            mayor=freqMap[Pattern]
    return mayor

Text="CGTTCCCAGACTAAGTTTGACTAAGTTTATCGCCCTGATCGCCCTGAGAAAAAGGTATCGCCCTGTCGTGTGGTCTCGTGTGGTCAGAAAAAGGTAGAAAAAGGTCGTTCCCACGTTCCCAAGAAAAAGGTTCGTGTGGTCAGAAAAAGGTATCGCCCTGATCGCCCTGATCGCCCTGGACTAAGTTTTCGTGTGGTCAGAAAAAGGTATCGCCCTGTCGTGTGGTCCGTTCCCAAGAAAAAGGTATCGCCCTGATCGCCCTGATCGCCCTGCGTTCCCAGACTAAGTTTCGTTCCCACGTTCCCAGACTAAGTTTTCGTGTGGTCATCGCCCTGGACTAAGTTTCGTTCCCAGACTAAGTTTGACTAAGTTTAGAAAAAGGTATCGCCCTGGACTAAGTTTAGAAAAAGGTATCGCCCTGAGAAAAAGGTGACTAAGTTTCGTTCCCAGACTAAGTTTCGTTCCCAGACTAAGTTTGACTAAGTTTTCGTGTGGTCCGTTCCCAGACTAAGTTTTCGTGTGGTCATCGCCCTGATCGCCCTGCGTTCCCAGACTAAGTTTGACTAAGTTTTCGTGTGGTCATCGCCCTGATCGCCCTGATCGCCCTGAGAAAAAGGTATCGCCCTGTCGTGTGGTCAGAAAAAGGTCGTTCCCAAGAAAAAGGTCGTTCCCAATCGCCCTGGACTAAGTTTAGAAAAAGGTGACTAAGTTTATCGCCCTGAGAAAAAGGTATCGCCCTGAGAAAAAGGTATCGCCCTGAGAAAAAGGTATCGCCCTGGACTAAGTTTAGAAAAAGGTTCGTGTGGTCTCGTGTGGTCCGTTCCCAATCGCCCTGGACTAAGTTTTCGTGTGGTCCGTTCCCATCGTGTGGTCATCGCCCTGATCGCCCTGAGAAAAAGGTATCGCCCTGAGAAAAAGGTCGTTCCCAAGAAAAAGGTCGTTCCCAATCGCCCTGTCGTGTGGTCCGTTCCCAAGAAAAAGGTAGAAAAAGGT"
Pattern="TAATTTTTA"
k=11
freqMap=FrequencyTable(Text,k)


# print(MaxMap(FrequencyTable(Text,k)))
print(BetterFrequentWord(Text,k))
# print(PatternCount(Text, Pattern))
        
