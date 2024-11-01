n=34 #number of generations
k=2 #pairs produce by each set of parents



producers=0
children=1
total=children
count =1

#only new parents produce childrenpring
while count < n:
    count+=1
    producers, children = children, total 
    total= children+producers*k 
    if count==n-1:
        print(total)
