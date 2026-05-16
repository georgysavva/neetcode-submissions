class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        state=[None]*(amount + 1)
        state[0]=0
        result=self.traverse(amount, state, coins)
        return result
    def traverse(self, node, state, coins):
        if node < 0:
            return -1
        if state[node] is not None:
            return state[node]
        best = None
        for coin in coins:
            result=self.traverse(node-coin, state, coins)
            if result != -1:
                best = result if best is None else min(best, result)
        state[node]=best + 1 if best is not None else -1
        return state[node]
        
        
        