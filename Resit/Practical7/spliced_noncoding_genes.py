input_gene=input("choose one from GTAG,GCAG,ATAC") #set the input for user to choose one of the three genes
input_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') #open the file containing the cDNA sequences of S.cerevisiae
outputfile_name=f"{input_gene}_spliced_genes.fa" #set the name of the output file
output_file=open(outputfile_name,'w')

def find_introns(sequence):
    donor=input_gene[0:2]
    acceptor=input_gene[2:4]
    pattern = f"(?=({donor}.*?{acceptor}))" #set the pattern to match the donor and acceptor sites of the input gene
    matches = re.findall(pattern, sequence) #find all the matches of the pattern in the sequence
    return f"Number of introns: {len(matches)}" #return the number of introns in the sequence


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
    if find_introns(sequence)!= f"Number of introns: 0": #check if the gene has any introns
        result=find_introns(sequence) #find the number of introns in the sequence
        output_file.write(f">{gene_name}\n{sequence}\n{result}\n") #write the gene name, sequence, and result to the output file

input_file.close()
output_file.close()