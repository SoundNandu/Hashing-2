Longest Palindrome:
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Time:O(n)
Space :O(1)

The logic is we iterate the elements of the string S.if we already have the value in the set we remove and increase the count+2 
else we add them in the hashset and if the hashset is greater than 0 we increment the count by 1 and return count 


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0
        hashset = set()
        count = 0
        for char in s:
            #print(char)
            if char in hashset:
                count += 2
                hashset.remove(char)
            else:
                hashset.add(char)
        if len(hashset) > 0:
            count += 1
        return count
                
