k=19
m=23
n=16

total=m+n+k

#find chance of each mate

rec_mate =  (n/(total))*((n-1))/(total-1)
hetero_mate= ((m/(total))*((m-1))/(total-1)) *0.25
hetero_rec_mate = ((n/(total))*(m/(total-1)) + (m/(total))*(n/(total-1))) *0.5
chance_rec = rec_mate + hetero_mate + hetero_rec_mate

#chance of dominant allele is 1 - chance of recessive allele

print(1-chance_rec)