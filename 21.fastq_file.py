from Bio import SeqIO

path="/home/rima/Desktop/biopython/control1.fastq"

record=SeqIO.parse(path,"fastq")

""" for data in record:
	print(data.id)
	#print(data.seq)
	print(data.letter_annotations["phred_quality"])"""
	
l1=[]
for s in record:
	l1.append(len(s.seq))
	
avg=sum(l1)/len(l1)
print("Average Lenghth",avg)
