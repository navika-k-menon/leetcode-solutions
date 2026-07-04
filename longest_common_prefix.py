# Difficulty: Easy
# Topic: String
#
# Approach:
# - Use the first string as a reference.
# - Compare each character with the corresponding character in every other string.
# - If a mismatch or the end of a word is reached, return the prefix found so far.
# - If all characters match, return the entire first string.
#
# Time Complexity: O(n × m)
# Space Complexity: O(1)
#
# where:
# n = number of strings
# m = length of the shortest string

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i, char in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]

        return strs[0]