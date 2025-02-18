#Solution to Rosalind problem "Inferring mRNA from Protein" https://rosalind.info/problems/mrna/

data = ( 
"""UUU F      CUU L      AUU I      GUU V
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
UGG W      CGG R      AGG R      GGG G""")

#create a list of codons and list of amino acid letters

dataList = data.split()

codons=[]
aminos=[]

for data in dataList:
	if len(data) == 3:
		codons.append(data)
	else:
		aminos.append(data)


#read data file of Amino Acids, create list of AAs

with open ("/Users/melissanolan/Downloads/rosalind_mrna.txt") as data: 
   prot= data.read().strip()

prot=list(prot)
prot.append("Stop")

possible_strings =1

#Count number of times an amino acid in seq is in the list derived from data

for i in prot:
	occs=aminos.count(i)
	possible_strings= possible_strings*occs 
	
# total number of different RNA strings from which the protein could have been translated, modulo 1,000,000	

print(possible_strings %1000000)
