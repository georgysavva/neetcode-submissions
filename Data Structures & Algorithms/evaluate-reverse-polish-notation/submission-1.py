class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val,_ = self.eval_rec(tokens)
        return val
    def eval_rec(self, tokens):
        operators = "+-*/"
        if tokens[-1] not in operators:
            return int(tokens[-1]), 1
        operator = tokens[-1]
        right_val, right_exp_len = self.eval_rec(tokens[:-1])
        left_val, left_exp_len = self.eval_rec(tokens[:-right_exp_len-1])
        if operator == '+':
            val = left_val + right_val
        elif operator == '-':
            val = left_val - right_val
        elif operator == '/':
            val = int(left_val / right_val)
        else:
            val = left_val * right_val
        return val, left_exp_len + right_exp_len + 1