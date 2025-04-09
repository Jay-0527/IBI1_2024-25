def Restriction_enzyme_cut_sites(sequence, recognition_sequence_of_restriction_enzyme): #function to find the cut sites of the restriction enzyme in the given sequence
    valid_nucleotides = {'A', 'C', 'G', 'T'} #set of valid nucleotides
    for i in sequence:
        if i not in valid_nucleotides:  #checking if the nucleotide is valid or not
            print("Invalid nucleotide found in the sequence")
            return None  #if invalid nucleotide is found, return None
    for i in recognition_sequence_of_restriction_enzyme:
        if i not in valid_nucleotides: #checking if the nucleotide is valid or not
            print("Invalid nucleotide found in the recognition sequence of the restriction enzyme")
            return None #if invalid nucleotide is found, return None
    cut_sites=[] #list to store the cut sites of the restriction enzyme in the given sequence
    enzyme_length=len(recognition_sequence_of_restriction_enzyme) #length of the recognition sequence of the restriction enzyme
    for i in range(len(sequence)-enzyme_length+1): #loop to iterate over the sequence
        if sequence[i:i+enzyme_length]==recognition_sequence_of_restriction_enzyme: #if the recognition sequence is found in the sequence
            cut_sites.append(i+1) #append the starting position of the cut site to the list

    for j in range(len(cut_sites)): #loop to convert the starting and ending positions of the cut sites to a string format
                
        start=cut_sites[j] #starting position of the cut site
        end=start+enzyme_length-1 #ending position of the cut site
        cut_sites[j]=f"{start}~{end}" #convert the starting and ending positions of the cut site to a string format
    return (", ".join(cut_sites)) #return the list of cut sites in a string format separated by commas
dna = "GGATCCGAGCTCGATCCGGATCC" #example DNA sequence
enzyme = "GGATCC"  #example restriction enzyme recognition sequence
print("DNA:", dna)
print("Enzyme:", enzyme)
print("Cut sites:", Restriction_enzyme_cut_sites(dna, enzyme)) #calling the function to find the cut sites of the restriction enzyme in the given sequence


    

    
