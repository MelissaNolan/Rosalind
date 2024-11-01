with open ("/Users/melissanolan/Downloads/rosalind_hamm.txt") as fasta:
	string1 = fasta.readline()
	string2 = fasta.readline()


#iterate over a string and compare each nucleotide at each index

error = 0
for nuc in range(len(string1)):
	if string1[nuc] == string2[nuc]:
		continue
	else : 
		error += 1
print (error)
