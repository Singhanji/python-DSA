#def first_occurance_word():
import re

a = input()
b = input()

res = re.search(a, b)

print(a.find(b+1))



#print(first_occurance_word(a,b))
#a,b = map(str, input()).split()
