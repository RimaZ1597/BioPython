from Bio import SeqIO

path="/home/rima/Desktop/python/file handling/sequence (1).fasta"

data=SeqIO.read(path,"fasta")
print(data)
print(data.id)

