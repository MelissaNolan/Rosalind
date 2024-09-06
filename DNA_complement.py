
file = open("/Users/melissanolan/Downloads/rosalind_revc.txt")
DNA = str(file.read())
DNA_reverse = DNA[::-1]
for nuc in DNA_reverse:
    if nuc == "A":
        print("T", end='')
    elif nuc == "T":
        print("A", end='')
    elif nuc == "C":
        print("G", end='')
    elif nuc == "G":
        print("C", end='')

