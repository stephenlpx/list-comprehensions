#basic example of list comprehensions and how it can be used to shorten code 

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
print(names)

#shortened version of the code
longnames = [name.upper() for name in names if len(name) > 5]
print(f"The Uppercase version of the long names is: {longnames}")

shortnames = [n.upper() for n in names if len(n) < 5]
print(f"The Uppercase version of the short names is: {shortnames}")

print("")

#this would be the code without using list comprehensions
long_names = []
for x in names:
    if len(x) > 5:
        long_names.append(x)
print(long_names)