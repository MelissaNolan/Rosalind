with open("/Users/melissanolan/Downloads/rosalind_cons-2.txt") as file:
    data=file.readlines()

matrix=[]
s=""
for a in data:
    if ">" in a:
        matrix.append(list(s))
        s=""
        continue
    else:
        s+=a.strip()
matrix.append(list(s)) #to add the last sequenxe in

matrix.pop(0)
#print(matrix)
#matrix assembled
columns=len(matrix[0])
rows=len(matrix)

#print(columns, rows) 

a=t=c=g=0
A=[]
T=[]
C=[]
G=[]


for i in range(columns):
    j=0
    while j<(rows):
        if matrix[j][i] =="A":
            a+=1
        elif matrix[j][i] =="T":
            t+=1
        elif matrix[j][i] =="C":
            c+=1
        elif matrix[j][i] =="G":
            g+=1
        j+=1
    else: #when j>rows
        A.append(a)
        T.append(t)
        C.append(c)
        G.append(g)
        a=t=c=g=0


consensus=""
for k in range(columns):
    if (A[k]>T[k]) and (A[k]>C[k]) and (A[k]>G[k]):
        consensus+= "A"
    elif (C[k]>T[k]) and (C[k]>A[k]) and (C[k]>G[k]):
        consensus+= "C"
    elif (T[k]>A[k]) and (T[k]>G[k]) and (T[k]>C[k]):
        consensus+= "T"
    elif (G[k]>T[k]) and (G[k]>C[k]) and (G[k]>A[k]):
        consensus+= "G"
    else:
        if max(A[k], C[k], G[k], T[k]) in A:
            consensus+= "A"
        elif max(A[k], C[k], G[k], T[k]) in C:
            consensus+= "C"
        elif max(A[k], C[k], G[k], T[k]) in T:
            consensus+= "T"
        elif max(A[k], C[k], G[k], T[k]) in G:
            consensus+= "G"
print(consensus, " ") 


print("A:", (" ".join(str(x) for x in A)), " ")
print("C:", (" ".join(str(x) for x in C)), " ")
print("G:", (" ".join(str(x) for x in G)), " ")
print("T:", (" ".join(str(x) for x in T)))

print(len(consensus))
print(columns)