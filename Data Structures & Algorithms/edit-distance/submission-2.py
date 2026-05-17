class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        state = {

        }
        return self.traverse(word1, word2, 0, 0, state)
    def traverse(self, word, target, i, j, state):
        if (i,j) in state:
            return state[(i,j)]
        if i >= len(word) and j >= len(target):
            return 0
        if i>=len(word):
            return len(target) - j
        if j>=len(target):
            return len(word) - i
        best = float('inf')
        if word[i] == target[j]:
            best = min(best, self.traverse(word, target, i+1, j+1, state))
        best = min(best, 1 + self.traverse(word, target, i+1, j+1, state)) # replace
        best = min(best, 1 + self.traverse(word, target, i, j+1, state)) # insert
        best = min(best, 1 + self.traverse(word, target, i+1, j, state)) # remove
        state[i, j ] = best
        return best

