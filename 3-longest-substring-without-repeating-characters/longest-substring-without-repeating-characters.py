class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Dictionary to store the last seen index of each character
        charIndex = {}
        # Variable to keep track of the start of the current window
        start = 0
        # Variable to keep track of the longest substring length
        LongestSubstring = 0

        for i, char in enumerate(s):
            # If the character is found in the dictionary and is within the current window
            if char in charIndex and charIndex[char] >= start:
                # Move the start of the window to the right of the previous occurrence of char
                start = charIndex[char] + 1

            # Update the last seen index of the character
            charIndex[char] = i
            # Calculate the length of the current substring and update maxLength if it's the longest found so far
            LongestSubstring = max(LongestSubstring, i - start + 1)

        return LongestSubstring
        