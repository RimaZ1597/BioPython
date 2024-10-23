from Bio import SeqIO

path="/home/rima/Downloads/ls_orchid.fasta"

data=SeqIO.parse(path,"fasta")

for record in data:
	print(record.id)
	print(record.seq)
