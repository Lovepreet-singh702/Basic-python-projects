def get_array():
    arr = list(map(int, input(f"Enter elements separated by space: ").split()))
    arr.sort()
    return arr

def binary_search(arr, n):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == n:
            return mid  
        elif arr[mid] < n:
            low = mid + 1  
        else:
            high = mid - 1  
    return -1  

arr = get_array()
n = int(input("Enter the value you want to search: "))

index = binary_search(arr, n)

if index != -1:
    print(f"{n} is present at index {index}")
else:
    print(f"{n} is not found in the array")
