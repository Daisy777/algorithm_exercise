# stack

```python
stack = []
# push
stack.append(2)
stack.append(3)

# pop 
stack.pop()
```

# queue

```python
# simple version with list
queue = []
# enqueue
queue.append(2)
queue.append(3)
# dequeue
queue.pop(0)
```

# heap
```python
>>> import heapq
>>> p = []
>>> heapq.heapify(p)
>>> heapq.heappush(p, (1, 'sdfsd'))
>>> heapq.heappush(p, (2, 'ss'))
>>> p
[(1, 'sdfsd'), (2, 'ss')]
>>> heapq.heappop(p)
(1, 'sdfsd')

'''
complexity to build a heap
O(n)
complexity to insert and delete 
O(logN)
```