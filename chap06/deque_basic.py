import collections

# キュー操作(末尾から要素を追加し、先頭から取り出す)
data = collections.deque()
data.append(10)
data.append(15)
data.append(30)
print(data)
print(data.popleft())
print(data)

# スタック操作(末尾から要素を追加し、末尾から取り出す)
data2 = collections.deque()
data2.append(10)
data2.append(15)
data2.append(30)
print(data2)
print(data2.pop())
print(data2)
