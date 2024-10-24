def search_rotated_array(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the mid element is the target
        if arr[mid] == target:
            return mid

        # Determine which side is sorted
        if arr[left] <= arr[mid]:  # Left side is sorted
            if arr[left] <= target < arr[mid]:  # Target is in the left sorted part
                right = mid - 1
            else:  # Target is in the right unsorted part
                left = mid + 1
        else:  # Right side is sorted
            if arr[mid] < target <= arr[right]:  # Target is in the right sorted part
                left = mid + 1
            else:  # Target is in the left unsorted part
                right = mid - 1

    # Target not found
    return -1

# Example usage
if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = search_rotated_array(arr, target)

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")
