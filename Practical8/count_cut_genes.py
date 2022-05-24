import re
#allow the users to input a filename as the new fasta file.
#Please note that this can only be done in python3 version
new_fasta_file = input("input a new filename:")
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
result = open(new_fasta_file,"w")
DNA = file.read()
DNA = "".join(DNA.split("\n"))
DNA = DNA.lstrip(">")
genes = re.split(r">",DNA)
output = " "
#show the name of the gene,the number of cuts made in this gene by EcoRI and the DNA sequence
for i in range(len(genes)):
              if re.search(r"GAATTC",genes[i]):
                  name = str(re.findall(r"gene:(.+?)\s",genes[i]))
                  name = name.strip("['']")
                  a = str(re.findall(r"](.+)",genes[i]))
                  a = a.strip("['']")
                  cuts_number = a.count("GAATTC")+1
                  output = output+">"+name+"\n"+"the number of fragments is"+" "+str(cuts_number)+"\n"+a+"\n"
result.write(output)
file.close()
result.close()

