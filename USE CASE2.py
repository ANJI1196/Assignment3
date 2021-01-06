# print Different vowels present in the given word:
element = input("Enter any word : ")
vowels =['a','e','i','o','u']
list1=[]
for x in element:
    if (x in vowels and x not in list1):
        list1.append(x)
print("Vowels present in the given word : ",list1)