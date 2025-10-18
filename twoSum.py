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
    n = len(arr)
    sumOfArr = sum(arr)
    sumOfN = (n*(n+1))//2
    return sumOfN - sumOfArr
def stringCompression(string):
    if not string:
        print("The string is empty")
    newString = ""
    prev = ''
    charCount = 1
    for ch in string:
        if ch == prev:
            charCount += 1
        else:
            if newString:
                newString += str(charCount)
                newString += ch
                charCount = 1
                prev = ch
            else:
                newString += ch
                prev = ch
    newString += str(charCount)
    return newString

# Input
choice = True
while (choice):
    print("\n")
    print("Welcome to the temple of logics\n 1.find Two sum \n 2. move zeros to the end\n 3.Find the missing number of the sequence\n 4.String Compression ! \n5. exit")
    while(True):
        try:
            need = int(input("Enter the choice you need: "))
            if need> 5 or need < 1:
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
    elif need == 4:
        string = input("Enter the string you need to compress: ")
        print(stringCompression(string))
        choice = input("Do you wanna continue ! (y/n) : ")
    if choice == "n" or need == 5:    
        break
    