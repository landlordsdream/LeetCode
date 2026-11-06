# LeetCode Solutions
## Git Commit 规范

本项目采用 [Conventional Commits](https://www.conventionalcommits.org/) 风格，提交信息格式：

- 动词开头，一般现在时
- 首字母小写，句尾不加句号
- summary 说清"改了什么"，让人半年后也能看懂

### 常用 type 前缀

| 前缀 | 含义 | 例子 |
|------|------|------|
| `feat:` | 新功能 / 新题解 | `feat: solve LeetCode 46 Permutations` |
| `fix:` | 修 bug | `fix: reset used flag after backtracking` |
| `docs:` | 文档/注释 | `docs: add backtracking explanation comments` |
| `refactor:` | 重构不改功能 | `refactor: extract backtracking template` |
| `test:` | 加测试 | `test: add cases for Permutations` |
| `chore:` | 杂项 | `chore: update .gitignore` |

### 动词库（挑一个开头）

| 场景 | 动词 |
|------|------|
| 做新题 | `solve` / `add` / `implement` |
| 修 bug | `fix` / `resolve` |
| 改逻辑 | `update` / `refactor` / `optimize` |
| 删代码 | `remove` / `delete` |
| 补注释 | `add` / `update` |
| 改名 | `rename` |

### 示例

```bash
git commit -m "feat: solve LeetCode 46 Permutations" -m "DFS backtracking with used array; copy path via path[:]; symmetric undo"
## 206. Reverse Linked List

### Recursive Approach — English Notes

**One-sentence summary**
> Recursively reverse the rest of the list, then make the next node point back to the current node.

**Steps**
1. **Base case**: If `head` is `None` or `head.next` is `None`, return `head`.
2. **Recursive step**: Call `reverseList(head.next)` to reverse the rest. It returns the new head.
3. **Rewire**: Set `head.next.next = head`.
4. **Break the old link**: Set `head.next = None` to avoid a cycle.
5. **Return**: Pass the new head back up the call stack.

### Vocabulary

| 中文 | English |
| --- | --- |
| 递归 | recursively / recursion |
| 终止条件 | base case |
| 空链表 | empty list |
| 单节点 | single node |
| 子链表 | sublist |
| 新头节点 | new head |
| 反转 | reverse |
| 指针 | pointer |
| 指向 | point to |
| 断开连接 | break the link |
| 形成环 | create a cycle |
| 调用栈 | call stack |
| 往回传 | pass back up |
| 分治 | divide and conquer |

### Key Phrases

- `reverse the rest of the list` — 反转剩余部分
- `return the new head` — 返回新头节点
- `make the next node point back to the current node` — 让下一个节点指回当前节点
- `set head.next.next = head` — 把 `head.next.next` 设为 `head`
- `avoid a cycle` — 避免成环
- `unwind the call stack` — 展开调用栈（递归往回走）
