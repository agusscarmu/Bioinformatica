def HammingDistance(text1, text2):
    distance=0
    for i in range(len(text1)):
        if text1[i]!=text2[i]:
            distance+=1
    return distance

def PatternsWHammingDistance(text, pattern, h):
    indices=[]
    n=len(text)
    k=len(pattern)
    for i in range(n-k+1):
        if HammingDistance(text[i:i+k],pattern)<=h:
            indices.append(i)
    return indices

def count(text, pattern, h):
    indices=PatternsWHammingDistance(text,pattern,h)
    count=len(indices)
    return count

text="AACAAGCTGATAAACATTTAAAGAG"
h=2
pattern="AAAAA"

print(count(text,pattern,h))