class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        # 栈 后进先出
        for ch in s:
            if ch in pairs: # 右括号
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop() # 匹配成功 弹出
            else:
                stack.append(ch)
        return not stack

