#First we open the text file to read the contents
f = open('CPLX2.txt', 'r')

seq = f.read()

f.close()

#Now we create a list with lines as elements of the list
seq_list = seq.split('\n')

#Remove the lines which starts with '>'
for element in seq_list:
    if element.startswith('>'):
        seq_list.remove(element)

#We join the elements to form the string sequence
sequence = ''.join(seq_list)

print('The number of adenine nucleotides is: ', sequence.count('A'))
print('The number of guanine nucleotides is: ', sequence.count('G'))
print('The number of thymine nucleotides is: ', sequence.count('T'))
print('The number of cytosine nucleotides is: ', sequence.count('C'))
