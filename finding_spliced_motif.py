with open("/Users/melissanolan/Downloads/rosalind_sseq-3.txt") as file :
    data =  file.readlines()
fastaDict = {}
fastaLabel = ""

for seq in data :
    if ">" in seq :
        fastaLabel = seq.strip()
        fastaDict[fastaLabel] = ""
    else :
        fastaDict[fastaLabel] += seq.strip()

s = str(max(fastaDict.values(), key = len))
t= str(min(fastaDict.values(), key = len))


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