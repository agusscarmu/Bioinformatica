def skew(text):
    skew=0
    s=[]
    s.append(skew)
    for nucl in text:
        if nucl == "C":
            skew-=1
        if nucl == "G":
            skew+=1
        s.append(skew)
    return s

def minSkew(text):
    skw=skew(text)
    minimo=min(skw)
    salida=[]
    for i in range(len(text)):
        if skw[i]==minimo:
            salida.append(i)
    return salida


text=open('./HiddingMsgDNA/dataset.txt').read()
t="GATACACTTCCCGAGTAGGTACTG"

print(minSkew(t))
