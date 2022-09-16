//A perfect number is a number which is equal to the sum of its proper divisors, i.e. all its divisors including 1 but not the number itself. 
For example, 6 = 3 + 2 + 1



n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
    
   

/*Auxiliary Space is the extra space or temporary space used by an algorithm.Space complexity includes both Auxiliary space and space used by input. */

