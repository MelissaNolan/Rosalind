#Solution to Rosalind problem "Open Reading Frames" https://rosalind.info/problems/orf/

#Iterate through every possible codon, initiate if M, and translate until Stop

def translation(mRNA):
    prot_chains = []
    codon = ""
    prot= ""
    for i in range(len(mRNA)-2):
        codon = mRNA[i:i+3]
        if codonDict[codon] == "M": 
            prot += codonDict[codon] 
            j = i+3 
            while j< (len(mRNA)-3): 
                codon = mRNA[j:j+3] 
                prot+= codonDict[codon]
                if codonDict[mRNA[j:j+3]] =="Stop":
                    prot= prot.replace("Stop", "")
                    prot_chains.append(prot)
                    prot=""
                    break
                j+=3 
    return prot_chains

#Find complementary strand

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

#transcribe

def transcription(strand):
    RNA=""
    RNA = strand.replace("T", "U")
    return RNA

#Codon dictionary data  

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

#Create codon dictionary

dataList = data.split()
codonDict = {}
for data in dataList:
	if len(data) == 3:
		codonName = data
		codonDict[codonName] = " "
	else:
		codonDict[codonName] = data
     
#Open data file containing title of DNA string and sequence

with open("/Users/melissanolan/Downloads/rosalind_orf.txt") as file:
    fastaLis=file.readlines()

newLis=[]
s=""
for line in fastaLis:
    line = line.strip()
    if ">" in line:
        continue
    else:
        s=line
        newLis.append(s)

DNA = "".join(newLis) 

#find reversed DNA strand, transcribe, do the same with original strand

rev_DNA = DNA[::-1]
rev_DNA = complement(rev_DNA)
rev_DNA = transcription(rev_DNA)

DNA = transcription(DNA)

#add the lists of every possible translation product for reverse and forward strand

final_list = translation(DNA) + translation(rev_DNA)
final_list = list(set(final_list))
for item in final_list:
  print(item)
print("\n")
