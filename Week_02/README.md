# 学习笔记

## 解题思路

### 树的遍历
可以用stack来完成pre-oder, in-order, post-order的遍历

- pre-order: pop栈顶元素，加入右子树，再加入左子树（因为后入先出，遍历完父亲就会遍历左子）
- in-order: 1)从root开始while循环以此入栈左子树 2)此时栈顶元素已经没有左子树，pop栈顶元素，while循环右子树的左子树加入到栈里
- post-order: pre-order的顺序是 父-左-右，post-order的顺序是左-右-父（反过来就是父-右-左），只要改变下pre-order的方向，再把最后结果的数组倒转就可以了

