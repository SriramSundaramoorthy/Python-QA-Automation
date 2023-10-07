#String - Nothing but a bunch of characters.
# Can be reprenseted by single quotes/ dobule quotes.

str_var="A"
print(str_var)

my_str_var = "'This is my String Variable'"
print(my_str_var)

#len function - To calculate the length of the strings. It includes whitespace as well.
# Length - Always starts from 1
# Index - Always start from 0 to length -1

print(len(my_str_var))

# Accessing String using Indexes.
print(my_str_var[4])

name="Sriram"

#Raw String - Print a string as it is.
print(r'C:\name')



#String Slicing:
#[A:B] - Starts from Index A to B-1. If B Index is more than the End Index, Then it will print all the characters.
print(name[0:10])
