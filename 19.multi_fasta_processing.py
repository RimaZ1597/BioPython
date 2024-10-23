from Bio import SeqIO

path="/home/rima/Downloads/ls_orchid.fasta"

data=SeqIO.parse(path,"fasta")

for record in data:
	print(record.id)
	print(record.seq)
	print("count A",record.seq.count("A"))
	print("count T",record.seq.count("T"))
	print("count G",record.seq.count("G"))
	print("count C",record.seq.count("C"))
	
