class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        cur_num = 0
        cur_str = ""
        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == '[':
                num_stack.append(cur_num)
                str_stack.append(cur_str)
                cur_num = 0
                cur_str = ""
            elif ch == ']':
                k = num_stack.pop()
                prev = str_stack.pop()
                cur_str = prev + cur_str*k
            else:
                cur_str = cur_str + ch

        return cur_str