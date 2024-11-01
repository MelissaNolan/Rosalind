mass = """A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333 """

#Create a dictionary of AA masses
mass_list = mass.split()
mass_dict = {}
AA_name = ""
for s in mass_list:
    if len(s) == 1:
        AA_name = s
        mass_dict[AA_name] = ""
    else:
        mass_dict[AA_name] = float(s.strip())

#Open file with AA sequence      
with open("/Users/melissanolan/Downloads/rosalind_prtm.txt") as file:
    pro = file.read()

pro_tup = tuple(pro.strip())

#Add the mass values for each amino acid in sequence
sum = 0
for val in pro_tup:
    if val in mass_dict.keys():
        sum += mass_dict[val]
    else:
        print("Error: key not found in dictionary")
print(sum)

