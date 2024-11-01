

with open("/Users/melissanolan/Downloads/rosalind_gc.txt") as fasta:
    fastaFile = fasta.readlines()
#create a dictionary with title of sequence(name) then code as value(seq), if > is in it then we assign FastaLabel to that name and create a value for it in our dictionary

fastaDict = {}
fastaLabel=""
for line in fastaFile:
	if '>' in line:
		fastaLabel = line.strip()
		fastaDict[fastaLabel] = " "
	else : 
		fastaDict[fastaLabel] += line.strip()

#compute GC content 
def find_GC(seq):
	return ((seq.count("G") + seq.count("C"))/ (len(seq)-1)*100)
#len seq -1 due to leading whitespace in fastadict i can't get rid of

#Create Results Dictionary 
resultDict = {fastaLabel: find_GC(seq) for (fastaLabel, seq) in fastaDict.items()}
greatest_gc = max(resultDict.values())

print([key for key, values in resultDict.items() if values==greatest_gc])
print (round(greatest_gc, 8))
