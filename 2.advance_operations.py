from Bio.Seq import Seq

s1=Seq("AGCCGTACGACGAGCATGCAGCGCAGTACGTACGTAGTCGTCAGTCAGTCAGTCAGTCAGTCAGTCACAGTACGTCAGTCAGTCAGCAGTAGCTGC")

print("original seq",s1)

#complement of seq

print("complement of seq",s1.complement())

#reverse complement

print("reverse complement",s1.reverse_complement())

#transcription

print("transcription",s1.transcribe())

#translate
print("translateee",s1.translate())
