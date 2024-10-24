def length_of_longest_substring(s):
    char_set = set()  # To store the characters in the current substring
    left = 0  # Left pointer for the sliding window
    max_length = 0  # Maximum length of substring found

    for right in range(len(s)):
        # If the character is already in the set, shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add the current character to the set
        char_set.add(s[right])
        
        # Calculate the length of the current substring and update max_length
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
if __name__ == "__main__":
    input_string = "abcabcbb"
    result = length_of_longest_substring(input_string)
    print(f"The length of the longest substring without repeating characters is: {result}")
