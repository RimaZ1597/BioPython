from Bio import Seq

#Bio   -> package Seq  -> program Seq.py

from Bio.Seq import Seq

#Bio ->pkg  .Seq -->program Seq ->class present in program

s1=Seq("TCGTCGTGTCATGATCGTCGTCGTGCGCTAAATACTCTTACTATGTGCTGTAGCTGACTGCTGTCGTCGATCGTGC")

print(s1)

print(type(s1))

print(s1[1])

print(s1[1:7])

print(s1[::-1])

print("count A",s1.count("A"))
print("count T",s1.count("T"))
print("count G",s1.count("G"))
print("count C",s1.count("C"))

print(len(s1))
