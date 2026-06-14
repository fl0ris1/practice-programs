#create a dictionary
countries={
    "Netherlands" : "Amsterdam",
    "Belgium" : "Brussels",
    "Germany" : "Berlin",
    "France" : "Paris"
}

print(countries)

#access a value from the dicitonary

print(f"Im going to {countries['Belgium']}")

#access all the keys from a dicitonary
keys_list=list(countries.keys())
print(keys_list)

#access all the values from the dictionary
values_list=list(countries.values())
print(values_list)

#looping through the dictionary and accessing keys and values

print("The keys in the dictionary are:")

for key in countries:
    print(key)

print("The values in the dicionary are: ")

for key in countries:
    print(countries[key])

#add a new key-value pair to the dictionary
countries["Italy"]="Rome"
print(countries)

#change a value in the dictionary
countries["Italy"]="Naples"
print(countries)

#delete a key value pair from the dictionary
del countries["France"]
print(countries)

