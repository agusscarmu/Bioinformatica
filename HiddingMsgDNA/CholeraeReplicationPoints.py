def posiblesPuntos(Text, Pattern):
    puntos=""
    k=len(Pattern)
    for i in range(len(Text)-k):
        if Pattern==Text[i:i+k]:
            puntos+=str(i)+" "
    return puntos

text=open('./Vibrio_cholerae.txt').read()
pattern="CTTGATCAT"
print(posiblesPuntos(text, pattern))