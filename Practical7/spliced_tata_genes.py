input_gene=input("choose one from GTAG,GCAG,ATAC") #set the input for user to choose one of the three genes
input_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') #open the file containing the cDNA sequences of S.cerevisiae
outputfile_name=f"{input_gene}_spliced_tata_genes.fasta" #set the name of the output file
output_file=open(outputfile_name,'w')
genes = {} #create an empty dictionary to store the cDNA sequences.
import re #import regular expression module

def count_tata_number(gene_sequence):
    count = 0  #initialize a counter to count the number of TATA motifs in the gene sequence
    for match in re.findall(r'TATA[AT]A[AT]', gene_sequence):
        count += 1 #increment the counter for each TATA motif found
    count=str(count) #convert the count to string
    return f"tata number in {gene_name} is {count}"

for lines in input_file:
    lines=lines.strip() #strip the newline character from the line
    if re.search(r'^>', lines): 
        genename=re.findall(r'gene:(\S+)', lines) #extract the gene name from the header line
        genes[genename[0]] = '' #set a variable for the key in the dictionary to the gene name
    else:
        genes[genename[0]] += lines #add the cDNA sequence to the value of the key in the dictionary

target_genes = {} #serves as a dictionary to store the target genes with TATA motifs
for gene_name, sequence in genes.items(): #
    if re.search(r'TATA[AT]A[AT]', sequence) and re.search(input_gene, sequence): #check if the gene has TATA motifs and if it matches the input gene
        target_genes[gene_name] = sequence   #add the gene to the target_genes dictionary
        result=count_tata_number(sequence)   #count the number of TATA motifs in the gene sequence
        output_file.write('>' + gene_name + '\n' + result + '\n' + sequence) #write the gene name, result and sequence to the output file

input_file.close()
output_file.close()