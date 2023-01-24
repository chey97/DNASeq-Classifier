
import re

#Function K-mers:
def Kmers_funct(seq,size):
    return [seq[x:x+size].lower() for x in range(len(seq) - size + 1)]

#Try it out with a simple sequence:
mySeq = ''
while True:
    mySeq = input("DNA sequence : ")
    
    if not re.match(r'^[A,C,G,T\s]+$', mySeq):
        print('Enter the DNA sequence using A,C,T,G')
        continue
    else:
        #print(mySeq)
        break
    
size = int(input("Enter the k-mer size : "))

print(Kmers_funct(mySeq,size))

#Join the kmers(words) into a single line:

joined_sentence = ''.join(Kmers_funct(mySeq,size))
# words = Kmers_funct(mySeq,size)
# joined_sentence = ''.join(words)
print(joined_sentence)

