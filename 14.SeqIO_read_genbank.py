from Bio import SeqIO

path="/home/rima/Desktop/biopython/sequence.gb"

data=SeqIO.read(path,"genbank")

#print(data)

print(data.id)
print(data.seq)
print(data.name)
print(data.description)
