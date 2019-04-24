f = open('dna.txt', 'r')

seq = f.read()

seq = seq.replace(' ', '').replace('\n', '').replace('\r', '')

print('The sequence we are going to analize is: ', seq)

#We create an ordered list of different elements of the sequence in order to know the different basis it contains
sorted_list = set(list(seq))

#Len of sequence
print('The total number of basis is: ', len(seq))

#Number of different basis
print('The number of different basis is : ', len(sorted_list))

#Count of basis
print('The number of adenine nucleotides is: ', seq.count('A'))
print('The number of guanine nucleotides is :', seq.count('G'))
print('The number of thymine nucleotides is:  ', seq.count('T'))
print('The number of cytosine nucleotides is: ', seq.count('C'))

f.close()