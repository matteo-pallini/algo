For binary search
```python
import bisect
foo = [1, 3, 5, 8, 9]
i = bisect.bisect(foo, 6) # i will be 3
i = bisect.bisect(foo, 5) # i will be 4
```

For heaps
```python
import heapq

foo = [3, 1, 4, 9, 2]
heapq.heapify(foo) # creates heap
min_val = heapq.heappop(foo) # returns 1
min_val = heapq.heappop(foo) # returns 2
# foo is now [3, 9, 4]
```
