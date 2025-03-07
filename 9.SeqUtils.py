from Bio.Seq import Seq
from Bio import SeqUtils

s1=Seq("""ATGACGACATCGTCCTACTTTCTGTTGGTGGCCCTAGGCCTTCTGCTGTACGTGTACGTGTGTCAATCTG
GCCAGGACTATTCCTGCCAGCTTGATGACCCTGCTGATCCACGGGGCAAATGTGGATCAGACTTGCCTGA
CTATCTCGAAAAAAAATGTGAAGAAGAGAAAGCTAGGCAAGGCGTTTCAGGAACAAATGACCCAGGGAAG
AAGAGAGGACGGGCTTCCCCACTGTTGAAGCGACGGCGCTTTCTCTCCATGATGAAGGCACGGGCCAAGA
GGAATGAACCATTTAAGCGGAGAGGTTACAAGGGAATTGCCTGTGAATGTTGTCAACATTACTGCACTGA
TCCAGAATTTACCAAGTATTGTCCCCCACTCCCTAAATCGTCCAGT""")

print("GC Percent",SeqUtils.GC(s1))

print("Molecular Weighgt ",SeqUtils.molecular_weight(s1))

