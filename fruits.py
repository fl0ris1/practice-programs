fruits={

}

for i in range(5):
    inp=input().lower()
    if inp not in fruits:
        fruits[inp]=1

    else:
        fruits[inp]+=1

print(fruits)