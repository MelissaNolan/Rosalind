#Solution to Rosalind problem "Calculating Expected Offspring" https://rosalind.info/problems/iev/

#Individuals with each phenotype in a population 

a=18260 #AA-AA
b=19745 #AA-Aa
c=18703 #AA-aa
d=16135 #Aa-Aa
e=19626 #Aa-aa
f=16327 #aa-aa

#formula for dominant phenotype presentation in next gen, given each couple has 2 offspring

expected= 2*(a+b+c+0.75*d+0.5*e)
print(expected)
