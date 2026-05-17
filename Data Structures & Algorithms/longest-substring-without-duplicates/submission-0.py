class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_substring = set()
        best = float('-inf')
        j=0
        for i in range(len(s)):
            letter = s[i]
            if letter not in curr_substring:
                curr_substring.add(letter)
                continue
            best = max(best,len(curr_substring))
            while j < i:
                letter_in_substring=s[j]
                j+=1
                curr_substring.remove(letter_in_substring)
                if letter_in_substring == letter:
                    break
            curr_substring.add(letter)
        best = max(best,len(curr_substring))
        return best
                

            
            