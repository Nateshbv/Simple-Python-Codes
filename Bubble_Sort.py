# python code to sort number 
# Bubble sort code for sorting the list of number without using the 
# inbuilt sort() function
def Bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1],arr[j]
    return arr
    
def main():
    numbers=[]
    
    n = int(input("How many numbers to sort? "))
    for k in range(0,n):
        j = int(input('numbers[' + str(k) + ']= '))
        numbers.append(j)
        
    print("the entered numbers are",numbers)
    print("the sorted numbers are",Bubble_sort(numbers))

if __name__== "__main__":
    main()
