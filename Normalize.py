def Normalize(Probabilities):
    total = sum(Probabilities.values())
    return {k: v/total for k, v in Probabilities.items()}

norm=Normalize({'a': 0.22, 'b': 0.54, 'c': 0.58, 'd': 0.36, 'e': 0.3})
print(norm)