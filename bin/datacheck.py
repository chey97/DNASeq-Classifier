from Bio import SeqIO
for sequence in SeqIO.parse('dna-sequence-dataset/example_dna.fa', "fasta"):
    print(sequence.id)
    print(sequence.seq)
    print(len(sequence))