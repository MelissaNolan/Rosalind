#Solution to Rosalind problem "Transcribind DNA into RNA" https://rosalind.info/problems/rna/

#Replaces T from DNA with U in resulting RNA

file = open("/Users/melissanolan/Downloads/rosalind_rna.txt")

DNA = str(file.read())
RNA = DNA.replace("T", "U")

print(RNA)
