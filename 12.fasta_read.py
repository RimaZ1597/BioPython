from Bio import SeqIO

path="/home/rima/Desktop/biopython/sequence (4).fasta"

data=SeqIO.read(path,"fasta")

#print(data)

print(data.id)
print(data.seq)
print(data.description)
