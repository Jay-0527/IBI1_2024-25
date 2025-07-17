input_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
output_file=open('noncoding_genes.fa','w')
genes = {}
import re
for lines in input_file:
    lines=lines.rstrip()
    if re.search(r'^>', lines):
        if 'gene_biotype:protein_coding' not in lines: #check if the gene is non-coding
            genename=re.findall(r'gene:(\S+)', lines) #extract the gene name from the header line
            genename=genename[0] #extract the gene name from the list of matches
            genes[genename] = '' #set a variable for the key in the dictionary to the gene name
        else:
            genename = None #if the gene is coding, set the variable to None
    else:
        if genename is not None: #if the gene is non-coding, add the sequence to the dictionary
            genes[genename] += lines #concatenate the sequence to the existing sequence in the dictionary
for gene_name, sequence in genes.items():  #iterate through the target gene names and sequences in the dictionary
    output_file.write('>' + gene_name + '\n' + sequence + '\n') #write the gene name and sequence to the output file
input_file.close()
output_file.close()

 