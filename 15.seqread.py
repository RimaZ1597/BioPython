from Bio import SeqIO

path="/home/rima/Desktop/biopython/sequence.gb"

data=SeqIO.read(path,"genbank")

#print(data)

#print(data.id)

#for i in data.features:
#	print (i.type,'----',i.location)
	
print(data.annotations)
