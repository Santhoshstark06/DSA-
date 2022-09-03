# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")

  
 #Time complexity: O(n)
#Auxiliary Space: O(1)

#Method using flag: In this method, the user compares each character from starting and ending in a for loop and if the character
#does not match then it will change the status of the flag. Then it will check the status of the flag and accordingly and print whether it is a palindrome or not. 

# Python program to check
# if a string is palindrome
# or not
st = 'malayalam'
j = -1
flag = 0
for i in st:
	if i != st[j]:
		flag = 1
		break
	j = j - 1
if flag == 1:
	print("NO")
else:
	print("Yes")
