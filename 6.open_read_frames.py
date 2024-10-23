from Bio.Seq import Seq

s1=Seq("GCATGCGTCGTCTCGATCACGACGAGCGCAGCATGATCGTCTACTGCCTGATCGTCGTCGTCGATGCTAGCTGCGCAGATAAAAAAAAAACTAGCTTCATGCAGCGCTCTAG")

print(s1)

print("1st frame: ",s1.translate())

print("2nd frame: ",s1[1:].translate())

print("3rd frame: ",s1[2:].translate())

rev= s1.reverse_complement()

print("4th frame: ",rev.translate())

print("5th frame: ",rev[1:].translate())

print("6th frame: ",rev[2:].translate())



