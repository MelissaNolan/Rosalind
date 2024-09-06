with open ("/Users/melissanolan/Downloads/rosalind_hamm.txt") as fasta:
	string1 = fasta.readline()
	string2 = fasta.readline()

#assign variables to the two strings
#iterate over a string and if string [pos] = string2[2], continue, else add a number

error = 0
for nuc in range(len(string1)):
	if string1[nuc] == string2[nuc]:
		continue
	else : 
		error += 1
print (error)
