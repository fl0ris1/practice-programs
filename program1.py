'''
take a string as input, check if its a palindrome string
'''

word=input()
word1=[]

palindrome=True
for i in range(len(word)-1,-1,-1):
    word1.append(word[i])

for i in range(0,len(word1)):
    if word1[i]!=word[i]:
        palindrome=False
        break


if palindrome:
    print("The word is a palindrome")

else:
    print("Not a palindrome")