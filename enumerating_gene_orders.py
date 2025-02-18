#Solution to Rosalind problem "Enumerating Gene Orders" https://rosalind.info/problems/perm/

from itertools import permutations
n=6

#create a list of integers from 1 to n

orders=[]
for i in range(1, n+1):
    orders.append(i)

#get permutations

perm = list(permutations(orders))
print(len(perm))

for x in perm:
    for j in x:
        print(" ".join(str(j) for j in x))
        break
