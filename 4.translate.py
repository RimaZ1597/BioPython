from Bio.Seq import Seq

s1=Seq("ACGTGACTGTCAGTGTGCTAGTCTGCTTCGTGACTGTACGTGCTGCTAGGGGGGATGCTATGCATGCGCTAGCTGGGGGGGGGGGGGGGGGGGCTAGTCGCC")

print("original seq",s1)

print(s1.translate()) 

print(s1.translate(stop_symbol="-"))

print(s1.translate(to_stop=True))

print(s1.translate(table=21))
