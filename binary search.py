arr = [1, 3, 5, 7, 9]
key = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Element found at position", mid)
        found = True
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if not found:
    print("Element not found")
