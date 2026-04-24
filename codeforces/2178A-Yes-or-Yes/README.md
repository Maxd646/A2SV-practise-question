# 2178A-Yes-or-Yes

**Problem:** [2178A-Yes-or-Yes](https://codeforces.com/contest/2178/problem/A)

**time limit per test:** 1 second

**memory limit per test:** 256 megabytes

---

Last Christmas, your friend Fernando gifted you a string s consisting only of the characters \mathtt{Y} and \mathtt{N}, representing "Yes" and "No", respectively.

You can repeatedly apply the following operation on s: 

 
-  Choose any two adjacent characters and replace them with their logical OR. 
Formally, in each operation, you can choose an index i (1 ≤q i ≤q |s|-1), remove the characters s_i and s_{i+1}, then insert:

 
-  A single \mathtt{Y} if at least one of s_i or s_{i+1} is \mathtt{Y}; 
-  A single \mathtt{N} if both s_i and s_{i+1} are \mathtt{N}. 
Note that after each operation, the length of s decreases by 1.

Unfortunately, Fernando does not want you to combine "Yes OR Yes", as he has experienced trauma relating to a certain song.

Determine whether it is possible to reduce s to a single character by repeatedly applying the operation above, without ever combining two \mathtt{Y}'s.


**Input**

Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows. 

The only line of each test case contains the string s (2≤ |s|≤ 100). It is guaranteed that s_i = \mathtt{Y} or \mathtt{N}.


**Output**

For each test case, print "YES" if the string can be reduced to a single character by repeatedly applying the described operation, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.


**Example**

**Input**

```
7
YY
NN
NNY
YYYNY
NNNNN
YYYYYY
YNNNNN
```

**Output**

```
NO
YES
YES
NO
YES
NO
YES
```


**Note**

In the first test case, you cannot combine s_1 and s_2 since they are both \mathtt{Y}. Thus, the answer is NO.

In the third test case, the following is a valid sequence of operations: \mathtt{NNY}\to\mathtt{NY}\to\mathtt{Y}. Thus, the answer is YES.

In the fourth test case, there are two possibilities for the first operation: \mathtt{YYYNY}\to \mathtt{YYYY} or \mathtt{YYYNY}\to \mathtt{YYYY}. However, in either case, it is not possible to perform any more operations without combining two \mathtt{Y}'s. Thus, the answer is NO.

In the fifth test case, the following is a valid sequence of operations: \mathtt{NNNNN}\to\mathtt{NNNN}\to\mathtt{NNN}\to\mathtt{NN}\to\mathtt{N}. Thus, the answer is YES.
