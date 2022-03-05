def count(elements): 
if elements[-1] == '.': 
elements = elements[0:len(elements) - 1] 
dictionary[elements] += 1
dictionary.update({elements: 1}) 
Sentence = "Mississippi"
dictionary = {} 
lst = Sentence.split() 
for elements in lst: 
count(elements)
for allKeys in dictionary:
print ("Frequency of ", allKeys, end = " ") 
print (":", end = " ") 
print (dictionary[allKeys], end = " ") 
print()
