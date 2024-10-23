from Bio import SeqIO

path="/home/rima/Desktop/biopython/control1.fastq"

record=SeqIO.parse(path,"fastq")

l1=[]
for s in record:
	l1.append(len(s.seq))
	
avg=sum(l1)/len(l1)

print("average length",avg)
