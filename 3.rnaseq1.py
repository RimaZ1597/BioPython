from Bio.Seq import Seq

r1=Seq("AGCCGUACGACGAGCAUGCAGCGCAGUACGUACGUAGUCGUCAGUCAGUCAGUCAGUCAGUCAGUCACAGUACGUCAGUCAGUCAGCAGUAGCUGCAGGCCUAGC")

print("Original Seq \n",r1)
print("Complement Seq \n",r1.complement())
print("Reverse Complement of Seq",r1.reverse_complement())
print("Rna seq into dna seq",r1.back_transcribe())
print("translation",r1.translate())
