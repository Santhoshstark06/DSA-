
#The bubble sort uses a straightforward logic that works by repeating swapping the adjacent elements if they are not in the right order. 
#It compares one pair at a time and swaps if the first element is greater than the second element; otherwise, move further to the next pair of elements for comparison.

def bubble_sort(list1):  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
         
        
    return list1  
  
list1 = [5, 3, 8, 6, 7, 2]  

print("The unsorted list is: ", list1) 

print("The sorted list is: ", bubble_sort(list1))  
