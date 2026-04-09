# 1691A-Beat-The-Odds

**Problem:** [1691A-Beat-The-Odds](https://codeforces.com/contest/1691/problem/A)

**time limit per test:** 1 second

**memory limit per test:** 256 megabytes

---

Given a sequence a_1, a_2, …, a_n, find the minimum number of elements to remove from the sequence such that after the removal, the sum of every 2 consecutive elements is even.


**Input**

Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases. Description of the test cases follows.

The first line of each test case contains a single integer n (3 ≤ n ≤ 10⁵).

The second line of each test case contains n integers a_1, a_2,…,a_n (1≤q a_i≤q10⁹) — elements of the sequence.

It is guaranteed that the sum of n over all test cases does not exceed 10⁵.


**Output**

For each test case, print a single integer — the minimum number of elements to remove from the sequence such that the sum of every 2 consecutive elements is even.


**Example**

**Input**

```
2
5
2 4 3 6 8
6
3 5 9 7 1 3
```

**Output**

```
1
0
```


**Note**

In the first test case, after removing 3, the sequence becomes [2,4,6,8]. The pairs of consecutive elements are \{[2, 4], [4, 6], [6, 8]\}. Each consecutive pair has an even sum now. Hence, we only need to remove 1 element to satisfy the condition asked.

In the second test case, each consecutive pair already has an even sum so we need not remove any element.
