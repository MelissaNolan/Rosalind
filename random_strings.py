import math
with open("/Users/melissanolan/Downloads/rosalind_prob-2.txt") as file:
    data = file.read()
data = data.split()

#our sequence is the first entry in data, gc content is further entries
seq = str(data[0])
data.pop(0)
gc_list = [float(x) for x in data]
matches_list = []

#calculate the probability of the string occurring for each given gc content
#use the common logarithm for very small numbers
for content in gc_list:
    prob_match = 0
    prob_gc = content/2
    prob_at=(1-content)/2
    for letter in seq:
        if letter == "A" or letter == "T":
            prob_match += math.log10(prob_at)
        elif letter == "C" or letter == "G":
            prob_match += math.log10(prob_gc)

    matches_list.append(round(prob_match, 3))

print((" ".join(str(j) for j in matches_list)))