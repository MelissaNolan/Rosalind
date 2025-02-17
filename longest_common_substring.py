
#Find the longest common substring 

with open("/Users/melissanolan/Downloads/rosalind_lcsm-3.txt") as file :
    data =  file.readlines()

#Create list of sequences
DNA = []
seq=""
for line in data:
    if ">" in line:
        DNA.append(seq)
        seq = ""
    else :
        seq += line.strip()
DNA.append(seq)
DNA.pop(0)
#print(DNA)


reference = max(DNA, key = len)

DNA.remove(reference)

substring = []

#Move a window along reference DNA and record it if all items in the list of sequences
#  contains it

for i in range(len(reference)) :
    for j in range(1 , len(reference)) :
        stem = reference[i:j]
        for k in range(0, len(DNA)) :
            if stem not in DNA[k] :
                break
            elif k == len(DNA) - 1 and len(stem) > 1 :
                substring.append(reference[i:j])

#Find the longest common substring

print(max(substring , key = len))
        
