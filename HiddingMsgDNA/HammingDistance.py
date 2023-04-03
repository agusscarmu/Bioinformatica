def HammingDistance(text1, text2):
    distance=0
    for i in range(len(text1)):
        if text1[i]!=text2[i]:
            distance+=1
    return distance

def PatternsWHammingDistance(text, pattern, h):
    indices=""
    n=len(text)
    k=len(pattern)
    for i in range(n-k+1):
        if HammingDistance(text[i:i+k],pattern)<=h:
            index=str(i)
            indices+=index+" "
    return indices


text="CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT"
text2="CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG"
pattern="TTCCTCCCTGTG"
h=5
print(HammingDistance(text,text2))
