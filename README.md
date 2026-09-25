# LeetCode 281 - Zigzag Iterator

## Problem Statement

Given two 1D vectors, `v1` and `v2`, implement an iterator to return their elements alternately.

The iterator should return elements in zigzag order.

For example:

```text
v1 = [1, 2]
v2 = [3, 4, 5, 6]

Output:
[1, 3, 2, 4, 5, 6]
```

The iterator should provide two functions:

* `next()` - Returns the next element.
* `hasNext()` - Returns `True` if there are still elements remaining.

---

## Example

### Input

```text
v1 = [1, 2]
v2 = [3, 4, 5, 6]
```

### Output

```text
[1, 3, 2, 4, 5, 6]
```

### Explanation

The elements are taken alternately:

```text
1 → from v1
3 → from v2
2 → from v1
4 → from v2
5 → remaining from v2
6 → remaining from v2
```

Therefore, the final output is:

```text
[1, 3, 2, 4, 5, 6]
```

---

## Approach

We use a queue to store iterators.

1. Add the iterators of `v1` and `v2` to a queue if they are not empty.
2. Remove the iterator from the front of the queue.
3. Get its next element.
4. If that iterator still has elements, put it back into the queue.
5. Continue until the queue becomes empty.

This allows the vectors to be processed alternately.

---

## Algorithm

1. Create an empty queue.
2. Add the iterator of `v1` if `v1` is not empty.
3. Add the iterator of `v2` if `v2` is not empty.
4. For `next()`:

   * Remove the first iterator from the queue.
   * Return its next element.
   * If more elements remain, add the iterator back to the queue.
5. For `hasNext()`:

   * Return `True` if the queue is not empty.
   * Otherwise return `False`.

---

## Example Walkthrough

```text
v1 = [1, 2]
v2 = [3, 4, 5, 6]
```

Initially:

```text
Queue:
[v1, v2]
```

After `next()`:

```text
Output: 1
Queue: [v2, v1]
```

After `next()`:

```text
Output: 3
Queue: [v1, v2]
```

After `next()`:

```text
Output: 2
Queue: [v2]
```

After `next()`:

```text
Output: 4
Queue: [v2]
```

Then:

```text
Output: 5
Output: 6
```

Final output:

```text
[1, 3, 2, 4, 5, 6]
```

---

## Time Complexity

For each element, the iterator performs constant-time queue operations.

**Time Complexity:** `O(n)`

where `n` is the total number of elements in both vectors.

---

## Space Complexity

The queue stores the active iterators.

**Space Complexity:** `O(k)`

where `k` is the number of non-empty vectors.

For two vectors, this is effectively `O(1)` auxiliary space.

---

## Key Concept

The main idea is to use a **queue of iterators** to maintain the zigzag order.

```text
v1 → v2 → v1 → v2 → ...
```

When one vector becomes empty, the remaining vector continues providing elements.

---

## Language

Python

## LeetCode Problem

281 - Zigzag Iterator

## Author

T. Nandhini
