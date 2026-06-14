'''
count occurences of all characters in a string
'''

word=input()
thisdict = {
}   

for i in range(0,len(word)):
    if word[i] not in thisdict:
        thisdict[word[i]] = 1

    else:
        thisdict[word[i]]+=1

print(thisdict)