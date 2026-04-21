# 2220A-Blocked

**Problem:** [2220A-Blocked](https://codeforces.com/contest/2220/problem/A)

**time limit per test:** 1 second

**memory limit per test:** 256 megabytes

---

Given an array a of integers of size n, we say that a position 1 ≤ i ≤ n is blocked if a_i can be expressed as the sum of a subset of a_1, a_2, …, a_{i-1} (i.e. there exist 1 ≤ j_1  \lt  j_2  \lt  …  \lt  j_k ≤ i-1 such that a_{j_1} + a_{j_2} + … + a_{j_k} = a_i). Reorder a so that no position is blocked or report that it is impossible.

For example, reordering the array [3, 2, 5] to [2, 3, 5] makes position 3 blocked, since we can express 5 = 2 + 3, but if we reorder it to [3, 5, 2], no position is blocked.


**Input**

Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 400). The description of the test cases follows. 

The first line of each test case contains an integer n (1 ≤ n ≤ 200).

The second line contains n integers, denoting the array a (\textbf{1} ≤ a_i ≤ 100).


**Output**

For each test case, print any order of a such that no position is blocked if it exists, otherwise print -1.


**Example**

**Input**

```
4
3
1 5 9
4
1 3 3 2
3
1 2 3
1
1
```

**Output**

```
5 9 1
-1
3 1 2
1
```


**Note**

In the third test case, the array [3, 1, 2] has no position blocked:

Position 1 is not blocked since 3 can't be expressed as the sum of a subset of [].

Position 2 is not blocked since 1 can't be expressed as the sum of a subset of [3].

Position 3 is not blocked since 2 can't be expressed as the sum of a subset of [3, 1].
