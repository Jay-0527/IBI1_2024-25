Seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' # Example sequence
import re
def find_introns(sequence): # Function to find total number of introns in a sequence
    pattern = r'(?=(GT.*?AG))' # Regular expression pattern to match introns
    matches = re.findall(pattern, sequence) # Find all matches of the pattern in the sequence
    return len(matches) # Return the number of matches found
print(f"Total possible introns: {find_introns(Seq)}")

