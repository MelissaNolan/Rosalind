def complement(strand):
    com=""
    for base in strand:
        if base =="A":
            com += "T"
        elif base =="T":
            com += "A"
        elif base =="C":
            com += "G"
        elif base =="G":
            com += "C"
    return com

with open() as file:
    data= file.readlines()

DNA=""
for line in data:
    if ">"in line:
        continue
    else:
        DNA+= line.strip()

comp_DNA=complement(DNA[::-1])
???

counter=1
matches=[]
for i in range (len(DNA)-1):
    site=[i:counter]
    if DNA[i:counter] in comp_DNA and 12>len(DNA[i:counter])>4:
        matches.append(DNA[i:counter])
