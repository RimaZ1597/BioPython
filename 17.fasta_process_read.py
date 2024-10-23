from Bio import SeqIO

path="/home/rima/Desktop/biopython/sequence (4).fasta"

data=SeqIO.read(path,"fasta")

print(data.id)
#print(data.seq)

print("count A",data.seq.count("A"))
print("count T",data.seq.count("T"))
print("count G",data.seq.count("G"))
print("count C",data.seq.count("C"))

#print(data.seq.translate())

print(len(data.seq))

