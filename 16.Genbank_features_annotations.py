from Bio import SeqIO

path="/home/rima/Desktop/biopython/sequence.gb"

data=SeqIO.read(path,"genbank")

print(data.id)

#print(data.features)

for i in data.features:
	print(i.type,'---',i.location)
	

print(data.annotations["taxonomy"])
