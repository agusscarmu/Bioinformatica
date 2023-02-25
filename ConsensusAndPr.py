
def Pr(Text,Profile):
    pro = 1
    for i in range(len(Text)):
        pro = pro*Profile[Text[i]][i]
    return pro

def Consensus(Profile):
    
    consensus = ""
    for j in range(len(Profile['A'])):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if profile[symbol][j] > m:
                m = profile[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

profile = {
    'A': [0.4,  0.3,  0.0,  0.1,  0.0,  0.9],
    'C': [0.2,  0.3,  0.0,  0.4,  0.0,  0.1],
    'G': [0.1,  0.3,  1.0,  0.1,  0.5,  0.0],
    'T': [0.3,  0.1,  0.0,  0.4,  0.5,  0.0]}
pr = Pr("CAGTGA",profile)
css = Consensus(profile)
print(pr)