Seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' # Example sequence
import re
def find_introns(sequence): # Function to find total number of introns in a sequence
    GT_position = [m.start() for m in re.finditer('GT', sequence)]
    AG_position = [m.start() for m in re.finditer('AG', sequence)]
    count = 0
    for i in range(len(GT_position)):
        for j in range(len(AG_position)):
            if (GT_position[i] < AG_position[j]):
                count += 1
    return count
print(f"Total possible introns: {find_introns(Seq)}")

