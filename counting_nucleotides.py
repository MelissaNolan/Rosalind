file = open("/Users/melissanolan/Downloads/rosalind_dna.txt")
DNA = file.read()
#Counts number of times A, T, C, G occur in given DNA sequence
A = 0
T = 0
C = 0
G = 0

for nuc in DNA:
    if nuc == "A":
        A += 1
    elif nuc == "T":
        T += 1
    elif nuc == "C":
        C += 1
    elif nuc == "G":
        G += 1
print(A , C, G, T)