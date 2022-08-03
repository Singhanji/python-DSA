# Program counting the frequency of element, Using DICTIONARY method of Python.
# TC: O(n)
# SC: O(1)

def freqOfElement(A):

# creating empty dictionary    
    freq = {}
    for item in A:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    if freq[item]>len(A)//2:
        print("The majority element is:", item)

    for k,v in freq.items():
        print("%d: %d" %(k,v))


#A = [3, 4, 4, 8, 4, 9, 4, 3, 4]
A =[2, 1, 2]
freqOfElement(A)

