#Solution to Rosalind problem "Consensus and Profile" https://rosalind.info/problems/cons/

with open("/Users/melissanolan/Downloads/rosalind_cons-3.txt") as file:
    data=file.readlines()

#Create a list of sequences

matrix=[]
s=""
for a in data:
    if ">" in a:
        if s:
            matrix.append(list(s))
        s=""
        continue
    else:
        s += a.strip()
if s:   #add last sequence
    matrix.append(list(s)) 

#Columns is the length of individual sequence and rows is how many DNA sequences there are

columns = len(matrix[0])
rows = len(matrix)

A, T, C, G = [], [], [], []

#read one index at a time in each sequence, record frequency of each nuc once the final sequence is reached

for i in range(columns):
    a=t=c=g=0
    for j in range(rows):
        if matrix[j][i] =="A":
            a+=1
        elif matrix[j][i] =="T":
            t+=1
        elif matrix[j][i] =="C":
            c+=1
        elif matrix[j][i] =="G":
            g+=1
    A.append(a)
    T.append(t)
    C.append(c)
    G.append(g)

#resolve any equalities in frequencies of nucleotides
#create consensus string

consensus=""
for k in range(columns):
    if A[k] >= max(T[k], C[k], G[k]):
        consensus += "A"
    elif C[k] >= max(A[k], T[k], G[k]):
        consensus += "C"
    elif G[k] >= max(A[k], T[k], C[k]):
        consensus += "G"
    else:
        consensus += "T"
print(consensus, " ") 


print("A:", (" ".join(str(x) for x in A)), " ")
print("C:", (" ".join(str(x) for x in C)), " ")
print("G:", (" ".join(str(x) for x in G)), " ")
print("T:", (" ".join(str(x) for x in T)))
