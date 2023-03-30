def HammingDistance(text1, text2):
    distance=0
    for i in range(len(text1)):
        if text1[i]!=text2[i]:
            distance+=1
    return distance

def AproximatePatternCount(text,pattern,h):
    count=0
    n=len(text)
    k=len(pattern)
    for i in range(n-k+1):
        patron=text[i:i+k]
        if HammingDistance(patron,pattern)<=h:
            count+=1
    return count

text="ATAGGAGTATCGGCGTCTTGTACCCGTGGAAGCGGTCGTTATTATTAACAGCGGCTTGCTATGGACACTTCTTGAACGATAATCAGTACCGCTGAGCGCGTATCCCGCTCCCATAGAGGTTCTCATAATAATCTGCCAGGAAGTTCCTCTACTGAGACAACGGCAACTCAGACTCCCGATCAGGTAGGCTCCTTACTTTTCGAGCGTTCCAAGCTCGTGGCAGCCCCGTGTACCTGTACTTCCACTCAAGTACGCGGGGGAGCTCAGCGGCCAACATGGAACGCGAGTCAGACGAGACCGCAGCTACTCCCACCAAGAAGCTGGAACGGTTCCCTATGAATT"
pattern="CAACAT"
h=2

print(AproximatePatternCount(text,pattern,h))