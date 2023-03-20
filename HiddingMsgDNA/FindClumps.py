import timeit
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

def FindClumps(Text,k,L,t):
    count=0
    p={}
    counted=[]
    n=len(Text)
    for i in range(n-L):
        p=FrequencyTable(text[i:i+L],k)
        for pattern in p:
            if pattern not in counted:
                if p[pattern]>=t:
                    counted.append(pattern)
    count=len(counted)

    return count

text=open('./E_Coli.txt').read()
# print("hola")
# print(text)
k=9
L=500
t=3

# print(FrequencyTable(text,k))
print(FindClumps(text,k,L,t))