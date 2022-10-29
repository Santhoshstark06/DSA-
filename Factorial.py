
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
num=int(input("Enter an integer number"))
#calling function
print("The factorial of",num,"is",factorial(num))





#Using build-in function
import math  
def fact(n):  
    return(math.factorial(n))  
  
num = int(input("Enter the number:"))  
f = fact(num)  
print("Factorial of", num, "is", f) 

