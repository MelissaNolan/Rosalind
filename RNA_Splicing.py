data = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

#Create Codon Dictionary
dataList = data.split()
codonDict = {}
for data in dataList:
	if len(data) == 3:
		codonName = data
		codonDict[codonName] = " "
	else:
		codonDict[codonName] = data
            
#Read FASTA document
with open("/Users/melissanolan/Downloads/rosalind_splc.txt") as file:
    fasta= file.readlines() 

#Create a dictionary of names and sequences
fastaDic = {}
fastaName = ""
for line in fasta:
    if ">" in line:
        fastaName = line.strip()
        fastaDic[fastaName] = ""
    else:
        fastaDic[fastaName] += line.strip()

fastaLis = list(fastaDic.values())

#Find the reference sequence and remove it from our list, remains are introns
DNA= max(fastaLis, key =len)
fastaLis.remove(DNA)

for intron in fastaLis:
    DNA = DNA.replace(intron, "")

#Find the RNA that will be translated after introns removed
ex_RNA = DNA.replace("T", "U")

#Create a list of codons read from RNA sequence
codons = [ ]
for base in range(len(ex_RNA)):
	if (base + 1) % 3 == 0:
		new_codon = ex_RNA[(base-2):(base+1)]
		codons.append(new_codon)

#Iterate through codons and find the amino acid code
AA_list = [codonDict[i] for i in codons]
AA_final = "".join(AA_list).replace("Stop", "")

print(AA_final)