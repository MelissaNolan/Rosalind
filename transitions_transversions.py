#Solution to Rosalind problem "Transitions and Transversions" https://rosalind.info/problems/tran/

def transitions(pair):
    if pair[0] == pair[1]:
        return False
    elif pair[0] == "A" and pair[1] == "G":
        return True
    elif pair[0] == "G" and pair[1] == "A":
        return True
    elif pair[0] == "T" and pair[1] == "C":
        return True
    elif pair[0] == "C" and pair[1] == "T":
        return True

def transversions(pair):
    if pair[0] == pair[1]:
        return False
    elif pair[0] == "A" and pair[1] == "G":
        return False
    elif pair[0] == "G" and pair[1] == "A":
        return False
    elif pair[0] == "T" and pair[1] == "C":
        return False
    elif pair[0] == "C" and pair[1] == "T":
        return False
    else:
        return True

with open("/Users/melissanolan/Downloads/rosalind_tran.txt") as file:
    fasta = file.readlines()


fastaList = []
s = ""
for data in fasta:
    if ">" in data:
        fastaList.append(s)
        s=""
    else:
        s += data.strip()
fastaList.append(s)

print(fastaList)

fastaList.pop(0)

s = fastaList[0]
t= fastaList[1]


numTransitions = len(list(filter(transitions, zip(s,t))))
numTransversions = len(list(filter(transversions, zip(s,t))))

ratio = numTransitions/ numTransversions
print(ratio)
