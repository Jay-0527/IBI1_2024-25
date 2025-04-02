input_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') #open the input file
output_file=open('tata_genes.fa','w') #open the output file
genes = {} #dictionary to store the gene sequences
import re #import regular expression module

for lines in input_file:
    lines=lines.strip() #remove the leading and trailing whitespaces
    if re.search(r'^>', lines): #if the line starts with '>'
        genename=re.findall(r'gene:(\S+)', lines) #extract the gene name from the header line
        genes[genename[0]] = '' #set a variable for the key in the dictionary to the gene name
    else:
        genes[genename[0]] += lines #add the sequence to the corresponding gene name in the dictionary

target_genes = {} #dictionary to store the target gene sequences
for gene_name, sequence in genes.items(): #iterate through the gene names and sequences in the dictionary
    if re.search(r'TATA[AT]A[AT]', sequence): #if the sequence contains the target sequence
        target_genes[gene_name] = sequence #add the gene name and sequence to the target gene dictionary

for gene_name, sequence in target_genes.items():  #iterate through the target gene names and sequences in the dictionary
    output_file.write('>' + gene_name + '\n' + sequence + '\n') #write the gene name and sequence to the output file

input_file.close()
output_file.close()
        



        
