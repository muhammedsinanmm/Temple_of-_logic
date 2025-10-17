def twoSum(arr, target):
    indexed_arr = sorted((num, i) for i, num in enumerate(arr))
    
    i = 0
    j = len(indexed_arr) - 1
    
    while i < j:
        total = indexed_arr[i][0] + indexed_arr[j][0]
        if total == target:
            return [indexed_arr[i][1], indexed_arr[j][1]]  # return original indices
        elif total > target:
            j -= 1
        else:  
            i += 1
    return []
def moveZeros(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
            
    return arr
def missingNumber(arr):
    if len(arr) != len(set(arr)):
        print("Invalid array input, duplicates exist!")
        return None
    
    xor = 0
    for i in range(len(arr)+1):
        xor ^= i
    for num in arr:
        xor ^= num
    return xor
# Input
choice = True
while (choice):
    print("\n")
    print("Welcome to the temple of logics\n 1.find Two sum \n 2. move zeros to the end\n 3.Find the missing number of the sequence\n 4. exit")
    while(True):
        try:
            need = int(input("Enter the choice you need: "))
            if need> 3 or need < 1:
                print("Enter a valid choice")
            else:
                break
        except ValueError:
            print("Enter a valid integer choice")
    
    if need == 1:
        
        li = list(map(int, input("Enter the list of numbers: ").split()))
        target = int(input("Enter the target value:"))

        print(twoSum(li, target))
        choice = input("Do you wanna continue (y/n): ").lower()

    elif need == 2:
        li = list(map(int, input("Enter the list of numbers: ").split()))

        print(moveZeros(li))
        choice = input("Do you wanna continue (y/n): ").lower()
    elif need == 3:
        li = list(map(int, input("Enter the list of numbers: ").split()))       
        print(missingNumber(li))
        choice = input("Do you wanna continue (y/n): ").lower()
    if choice == "n" or need == 4:    
        break
    #its been a while to enter but trust me im on it and i will mke it look cool