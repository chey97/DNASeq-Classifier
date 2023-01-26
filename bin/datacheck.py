'''
- This program was build for academic purpose - DNASeq - DNA Sequence Classifier Copyright (C) 2023  Chethiya Galkaduwa
'''

from Bio import SeqIO
for sequence in SeqIO.parse('dna-sequence-dataset/example_dna.fa', "fasta"):
    print(sequence.id)
    print(sequence.seq)
    print(len(sequence))