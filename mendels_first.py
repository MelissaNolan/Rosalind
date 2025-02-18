#Solution to Rosalind problem "Mendel's First Law" https://rosalind.info/problems/iprb/

k = 19 #homozygous dominant
m = 23 #heterozygous
n = 16 #homozygous recessive

total = m + n + k

#find chance of each mate

rec_mate =  (n/(total))*((n-1))/(total-1)
hetero_mate= ((m/(total))*((m-1))/(total-1)) *0.25
hetero_rec_mate = ((n/(total))*(m/(total-1)) + (m/(total))*(n/(total-1))) *0.5
chance_rec = rec_mate + hetero_mate + hetero_rec_mate

#chance of dominant allele is 1 - chance of recessive allele
#The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele
# any two organisms can mate.

print(1-chance_rec)
