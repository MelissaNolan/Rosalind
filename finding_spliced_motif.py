#Solution to Rosalind problem "Finding a Spliced Motif" https://rosalind.info/problems/sseq/

with open("/Users/melissanolan/Downloads/rosalind_sseq-3.txt") as file :
    data =  file.readlines()
    
#Create Fasta Dictionary with names, sequences

fastaDict = {}
fastaLabel = ""

for seq in data :
    if ">" in seq :
        fastaLabel = seq.strip()
        fastaDict[fastaLabel] = ""
    else :
        fastaDict[fastaLabel] += seq.strip()

#Find the main string and substring

s = str(max(fastaDict.values(), key = len))
t= str(min(fastaDict.values(), key = len))

#Find the indices of s where t is a subsequence

counter = 0
indice = 0

for i in range(len(s)) :
    if s[i] == t[counter] :
        print( i + 1 , end = " ")
        counter += 1
        if counter > len(t) - 1 :
            break
    else :
        continue

print("\n")
