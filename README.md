# LeetCode Solutions
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
