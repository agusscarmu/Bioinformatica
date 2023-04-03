def MotifEnumeration(Dna, k, d):
    patterns = set()
    for seq in Dna:
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            neighbors = neighbors_with_mismatches(kmer, d)
            for neighbor in neighbors:
                if all([contains_with_mismatches(s, neighbor, d) for s in Dna]):
                    patterns.add(neighbor)
    return list(patterns)

def neighbors_with_mismatches(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighbors = []
    suffix_neighbors = neighbors_with_mismatches(pattern[1:], d) #Uso de recursividad para tomar todos los neighbors posibles
    for neighbor in suffix_neighbors:
        if hamming_distance(pattern[1:], neighbor) < d:
            for base in ['A', 'C', 'G', 'T']:
                neighbors.append(base + neighbor)
        else:
            neighbors.append(pattern[0] + neighbor)
    return neighbors

def hamming_distance(s1, s2):
    return sum([c1 != c2 for c1, c2 in zip(s1, s2)])

def contains_with_mismatches(s, pattern, d): # 's' hace referencia a la cadena de adn que esta revisando en ese momento
    for i in range(len(s) - len(pattern) + 1):
        if hamming_distance(s[i:i+len(pattern)], pattern) <= d:
            return True
    return False


text = [
    "CGGAACTAACTACATCCTGAGCTTA", 
    "TGCAAATCGATGCTGGGTTACGTGT", 
    "ACCAATCCTCGCTTAGCCGGTGCAT", 
    "AGTATGCTATGTTTAGGCTACCGGG", 
    "GGGTCGGTTATGCAAGACGTATATA",
    "GGGTGAACCGCATAAGATTAGTTAC"
]
k=5
d=1
print(MotifEnumeration(text,k,d))