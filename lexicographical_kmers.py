#Solution to Rosalind problem "Enumerating k-mers Lexicographically" https://rosalind.info/problems/lexf/

from itertools import product
with open("/Users/melissanolan/Downloads/rosalind_lexf-2.txt") as file:
    text = file.readlines()

alphabet = ""

#Create the ordered alphabet from file

for item in text:
    item = item.strip().replace(" ", "")
    alphabet += item

#remove the last entry in the string, the postiive integer to rep length of solution

n = int(alphabet[-1:])

alphabet = alphabet[:-1]

#use cartesian product to find all combinations with repeats

combos = product(alphabet, repeat=n)
for x in combos:
    print( "".join(y for y in x))
