#Solution to Rosalind problem "Locating Restriciton Sites" https://rosalind.info/problems/revp/

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

with open("/Users/melissanolan/Downloads/rosalind_revp.txt") as file:
   data= file.readlines()
    
#define DNA sequence

DNA = ""
for line in data:
    if ">"in line:
        continue
    else:
        DNA += line.strip()

matchesIndex = []
matchesLength = []
comp_DNA=complement(DNA)

counter = 1

#Create a sliding window to compare original strand and complement strand, record if theres restriciton site

for i in range(len(DNA)) :
    for j in range(i + 3 , i + 13) :
        if j > (len(DNA)) :
            break
        elif DNA[i:j] == comp_DNA[j:i:-1] :
            matchesIndex.append(i + 1)
            matchesLength.append(len(DNA[i:j]) + 1)

res = list(zip(matchesIndex , matchesLength))

#Formatting solution of position and length of every palindrome 4<= length >= 12
for tuple in res:
    for item in tuple:
        print(item, end = " ")
    print("\n")
