#Solution to Rosalind problem "Finding a Motif in DNA" https://rosalind.info/problems/subs/

with open ("/Users/melissanolan/Downloads/rosalind_subs-2.txt") as data: 
   data = data.read()
DNA_s_main , DNA_t_substring = data.splitlines()
 
comber = 0

#find location of substring in main DNA

while comber < len(DNA_s_main) : 
   if comber == DNA_s_main.find(DNA_t_substring, comber) :
      print (comber +1)
   comber += 1   
