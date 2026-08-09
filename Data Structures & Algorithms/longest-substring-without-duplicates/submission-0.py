class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary stores the most recent index where
        # each character was seen.
        last_seen = {}

        # Left side of our current "window"
        left = 0

        # Keep track of the longest valid substring we've found
        max_length = 0

        # right moves through the string one character at a time
        for right in range(len(s)):
            char = s[right]

            # If we've seen this character before AND
            # its previous position is inside our current window,
            # we have a duplicate.
            if char in last_seen and last_seen[char] >= left:

                # Move left to one position after the previous
                # occurrence of this character.
                left = last_seen[char] + 1

            # Update the character's most recent position.
            last_seen[char] = right

            # Current window is from left -> right.
            current_length = right - left + 1

            # Update the maximum if this window is longer.
            max_length = max(max_length, current_length)

        return max_length