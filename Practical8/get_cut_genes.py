import re
import os
os.chdir("/Users/macbook/IBI1_2021-22/Practical8")
all_genes = open ("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
result = open("cut_genes.fa","w")
seq = all_genes.read()
seq = " ".join(seq.split("/n"))
seq = seq.lstrip(">")
genes = re.split(r">",seq)
output = " "
for i in range (len(genes)):
    if re.search(r"GAATTC",genes[i]):
        name = str(re.findall(r"genes:(.+?)\s",genes[i]))
        a = str(re.findall(r"](.+)",genes[i]))
        a = a.strip("[" "]")
        length = len(a)
        output = output+">"+name+"length"+"\n"+a+"\n"
output = output[:-1]               
result.write(output)
all_genes.close()
result.close()
