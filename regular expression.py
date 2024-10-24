def is_match(text, pattern):
    def match_helper(i, j):
        if j == len(pattern):
            return i == len(text)

        first_match = i < len(text) and pattern[j] in {text[i], '.'}

        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            return match_helper(i, j + 2) or (first_match and match_helper(i + 1, j))
        else:
            return first_match and match_helper(i + 1, j + 1)

    return match_helper(0, 0)

# Example usage:
print(is_match("aab", "c*a*b"))  # Output: True
print(is_match("mississippi", "mis*is*p*."))  # Output: False