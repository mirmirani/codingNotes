#preamble: 
# Abstract data types & lists
my_list = [11,13,17,"Python",67,[91,87]]
print(my_list[3])
#Conditional Logic
age = int(input("How Old Are You?"))

if age >= 18:
    print("Access allowed")
elif age < 18 and age > 0:
    print("Access not allowed")
else:
    print("invalid input")

#Dictionaries - Dictionary, Key, Value
Book = {
    "author": "Khalid Williams",
    "ISBN": 123456,
    "Genre": ['Biography','Religion']    
}
#print keys
# example to print key in dictionary
for author in Book:
    print(author)
#print key values
for Genre in Book:
    print(Book[Genre])
