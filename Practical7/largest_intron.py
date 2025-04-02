seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' #Set the sequence
import re #Import regular expression module
result1 = re.findall(r'GT.+AG',seq) #Find all the sequences of the form GT followed by any character and AG
print(result1)