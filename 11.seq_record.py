from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

S1=SeqRecord(Seq("ATTTTGGGCGGCGGG"),id="6789",name="ASGH",description="Protein")

#print (S1)

print (S1.id)
print (S1.name)
