from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

s1=SeqRecord(Seq("ACGTTGCTGTAGTGCTTCGATCGATCGTCGTGCATGCTGCTCT"),id="NC888",name="ABCD",description="toxic membrane protein")

#print(s1)

print(s1.id)
print(s1.seq)
print(s1.description)
