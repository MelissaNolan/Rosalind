
from itertools import product
with open("/Users/melissanolan/Downloads/rosalind_lexf-2.txt") as file:
    text = file.readlines()

alphabet = ""

#Create the alohabet
for item in text:
    item = item.strip().replace(" ", "")
    alphabet += item

#remove the last entry in the string
n = int(alphabet[-1:])
alphabet = alphabet[:-1]


#use cartesian product to find all combinations with repeats

combos = product(alphabet, repeat=n)
for x in combos:
    print( "".join(y for y in x))
