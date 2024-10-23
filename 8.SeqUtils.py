from Bio.Seq import Seq
from Bio import SeqUtils
s1=Seq("AAGTTGCGCGCGATttATGAGAAGAGCGCGCGGTTGTGAACCGGCCGGTTGTGGAGAATGTGGCCGCGACCACAATTAGAGAGTAGTATGC")

print(SeqUtils.GC(s1))


print(SeqUtils.molecular_weight(s1))

