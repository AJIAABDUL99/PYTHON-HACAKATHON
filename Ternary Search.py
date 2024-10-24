def ternary_search(arr, left, right, target):
    if right >= left:
        # Dividing the array into three parts
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Check if the target is present at mid1
        if arr[mid1] == target:
            return mid1
        # Check if the target is present at mid2
        if arr[mid2] == target:
            return mid2

        # If target is less than mid1, search in the left part
        if target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)
        # If target is greater than mid2, search in the right part
        elif target > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, target)
        # If target is in the middle part, search between mid1 and mid2
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)

    # Target is not found
    return -1

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    result = ternary_search(arr, 0, len(arr) - 1, target)

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")
