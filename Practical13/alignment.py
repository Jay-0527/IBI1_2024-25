#length of amino acids: 222
#subcellular location: Mitochondrial Matrix
#hits: 250
#percentage identities: 58.1%~100%

from Bio import SeqIO
from Bio.Align import substitution_matrices

def calculate_alignment_score(seq1, seq2):
    blosum62 = substitution_matrices.load("BLOSUM62")
    print(blosum62)
    score = 0
    for aa1, aa2 in zip(seq1, seq2):
        score += blosum62[aa1][aa2]
    return score

def calculate_identity_percentage(seq1, seq2):
    identical = 0
    for aa1, aa2 in zip(seq1, seq2):
        if aa1 == aa2:
            identical += 1
    return (identical / len(seq1)) * 100

human_seq = SeqIO.read(r"C:\Users\71588\Desktop\IBI1_2024-25\Practical13\human.fasta", "fasta")
mouse_seq = SeqIO.read(r"C:\Users\71588\Desktop\IBI1_2024-25\Practical13\mouse.fasta", "fasta")
ransom_seq = SeqIO.read(r"C:\Users\71588\Desktop\IBI1_2024-25\Practical13\random.fasta", "fasta")

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


