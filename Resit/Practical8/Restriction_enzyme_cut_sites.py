def find_restriction_sites(dna_sequence, enzyme_sequence):
    valid_nucleotides = {'A', 'C', 'G', 'T'} # Valid nucleotides for DNA sequences
    if not all(nuc in valid_nucleotides for nuc in dna_sequence):
        return "Error: DNA sequence contains invalid nucleotides" # Check if all nucleotides are valid
    if not all(nuc in valid_nucleotides for nuc in enzyme_sequence):
        return "Error: Enzyme recognition sequence contains invalid nucleotides" # Check if all nucleotides are valid
    if len(enzyme_sequence) > len(dna_sequence):
        return "Error: Enzyme recognition sequence is longer than the DNA sequence" # Check if enzyme sequence is shorter than the DNA sequence
    cut_sites = [] # List to store the cut sites
    for i in range(len(dna_sequence) - len(enzyme_sequence) + 1): # Iterate over all possible cut sites
        if dna_sequence[i:i+len(enzyme_sequence)] == enzyme_sequence:
            cut_sites.append(i+1) # Add the index of the cut site to the list
    if not cut_sites:
        return "No restriction sites found" # If no cut sites are found, return a message
    return cut_sites 
# Example usage:
print(find_restriction_sites("GTGTCTATCGTCACAAATCGGTAC", "ATCG")) # Output: [7, 17]