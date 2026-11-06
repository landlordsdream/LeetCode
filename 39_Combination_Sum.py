class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []
        candidates.sort()

        def dfs(start, current_sum):
            if current_sum == target:
                res.append(path[:])
                return
            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                if current_sum + candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i, current_sum + candidates[i])   # 传 i 可重复选
                path.pop()

        dfs(0, 0)
        return res