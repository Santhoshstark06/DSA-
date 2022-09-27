
txt = "Hello World"[::-1]
print(txt)
#O/P -- dlroW olleH

# Function to reverse a string
def reverseString(s):

   reversedString = ""

   for char in s:

       reversedString = char + reversedString

   return reversedString

s = str(input("Enter a string:"))
print("The reversed string is - ", reverseString(s))

#O/P --


#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, World!"
print(b[2:5])

#0/p -- llo

b = "Hello, World!"
print(b[:5])
#O/P -- Hello

b = "Hello, World!"
print(b[2:])

#O/P -- llo,world
