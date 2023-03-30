import timeit
# Nos da un diccionario con la cantidad de frecuencia de un patron en un segmento de ADN
def FrequencyTable(patterns):
    salida={}
    for i in range(len(patterns)):
        salida[patterns[i]]+=1
    return salida

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

def Patterns(text,k):
    p=[]
    for i in range(len(text)):
        pattern=text[i:i+k]
        p.append(pattern)
    return p


def FindClumps(Text,k,L,t):
    salida={}
    patterns=Patterns(Text,k)
    for i in range(len(Text)-L):
        freqTab=FrequencyTable(patterns[i:i+L])
        for Pattern in freqTab:
            if freqTab[Pattern]>=t:
                salida[Pattern]+=1
    return salida

text=open('./HiddingMsgDNA/E_Coli.txt').read()
# print("hola")
# print(text)
k=9
L=500
t=3

# print(FrequencyTable(text,k))
print(FindClumps(text,k,L,t))