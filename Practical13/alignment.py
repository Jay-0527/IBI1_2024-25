from Bio import SeqIO # import SeqIO module from Bio package
from Bio.Align import substitution_matrices # import certain substitution matrices

def calculate_alignment_score(seq1, seq2):
    blosum62 = substitution_matrices.load("BLOSUM62") # load BLOSUM62 matrix
    seq1 = seq1.upper() # convert sequences to uppercase
    seq2 = seq2.upper()
    score = 0  # Set initialize score to 0.
    for aa1, aa2 in zip(seq1, seq2): # iterate over the sequences and calculate the score.
        score += blosum62[aa1][aa2] # add the score of the current pair of amino acids to the total score.
    return score

def calculate_identity_percentage(seq1, seq2):
    identical = 0 # Set initialize identical to 0.
    seq1 = seq1.upper() # convert sequences to uppercase
    seq2 = seq2.upper()
    for aa1, aa2 in zip(seq1, seq2): # iterate over the sequences and calculate the number of identical amino acids.
        if aa1 == aa2:
            identical += 1 # add 1 to the number of identical amino acids if the current pair of amino acids are identical.
    return (identical / len(seq1)) * 100 # calculate and return the identity percentage.

human_seq = SeqIO.read(r"C:\Users\71588\Desktop\IBI1_2024-25\Practical13\human.fasta", "fasta") # read in the human sequence.
mouse_seq = SeqIO.read(r"C:\Users\71588\Desktop\IBI1_2024-25\Practical13\mouse.fasta", "fasta") # read in the mouse sequence.
ransom_seq = SeqIO.read(r"C:\Users\71588\Desktop\IBI1_2024-25\Practical13\random.fasta", "fasta") # read in the random sequence.

#human vs mouse
print("Human vs Mouse")
score = calculate_alignment_score(str(human_seq.seq), str(mouse_seq.seq))
print("Alignment score:", score)
identity_percentage = calculate_identity_percentage(str(human_seq.seq), str(mouse_seq.seq))
print(f"Identity percentage: {identity_percentage:.2f}% \n")

#human vs random
print("Human vs Random")
score = calculate_alignment_score(str(human_seq.seq), str(ransom_seq.seq))
print("Alignment score:", score)
identity_percentage = calculate_identity_percentage(str(human_seq.seq), str(ransom_seq.seq))
print(f"Identity percentage: {identity_percentage:.2f}% \n")

#mouse vs random
print("Mouse vs Ransdm")
score = calculate_alignment_score(str(mouse_seq.seq), str(ransom_seq.seq))
print("Alignment score:", score)
identity_percentage = calculate_identity_percentage(str(mouse_seq.seq), str(ransom_seq.seq))
print(f"Identity percentage: {identity_percentage:.2f}%")


