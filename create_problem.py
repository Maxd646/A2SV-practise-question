import os
import subprocess

def slugify(text):
    return text.strip().replace(" ", "-")

def create_files(base, folder, filename, title, platform):
    path = os.path.join(base, folder)
    os.makedirs(path, exist_ok=True)

    # ---- Solution template ----
    solution_template = f"""# {title}
# Platform: {platform}

for _ in range(int(input())):
    input()
    s= input()
    if "aa" in s:
         print(2)
    else:
        if  "aca" in s or "aba" in s:
            print(3)
        elif  "abca" in s or "acba" in s:
            print(4)
        elif "abbacca" in s or "accabba" in s:
            print(7)
        else:
            print(-1)
          
"""

    # ---- README template ----
    readme_template = f"""# {title}

## Platform
{platform}

## C. Dominant Character

Ashish has a string s
 of length n
 containing only characters 'a', 'b' and 'c'.

He wants to find the length of the smallest substring, which satisfies the following conditions:

Length of the substring is at least 2
'a' occurs strictly more times in this substring than 'b'
'a' occurs strictly more times in this substring than 'c'
Ashish is busy planning his next Codeforces round. Help him solve the problem.

A string a
 is a substring of a string b
 if a
 can be obtained from b
 by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

Input
The first line contains a single integer t
 (1≤t≤105)
  — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer n
 (2≤n≤106)
  — the length of the string s
.

The second line of each test case contains a string s
 consisting only of characters 'a', 'b' and 'c'.

It is guaranteed that the sum of n
 over all test cases does not exceed 106
.

Output
For each test case, output the length of the smallest substring which satisfies the given conditions or print −1
 if there is no such substring.

Example
InputCopy
3
2
aa
5
cbabb
8
cacabccc
OutputCopy
2
-1
3
Note
Consider the first test case. In the substring "aa", 'a' occurs twice, while 'b' and 'c' occur zero times. Since 'a' occurs strictly more times than 'b' and 'c', the substring "aa" satisfies the condition and the answer is 2
. The substring "a" also satisfies this condition, however its length is not at least 2
.

In the second test case, it can be shown that in none of the substrings of "cbabb" does 'a' occur strictly more times than 'b' and 'c' each.

In the third test case, "cacabccc", the length of the smallest substring that satisfies the conditions is 3
.


"""

    # ---- NOTES template ----
    notes_template = "# Notes\n\n- Observations\n- Mistakes\n"

    #  Write files with UTF-8 encoding
    with open(os.path.join(path, f"{filename}.py"), "w", encoding="utf-8") as f:
        f.write(solution_template)

    with open(os.path.join(path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_template)

    with open(os.path.join(path, "NOTES.md"), "w", encoding="utf-8") as f:
        f.write(notes_template)

    print(" Created:", path)

    # --- Open VS Code automatically ---
    try:
        subprocess.run(["code", path])
    except:
        print(" VS Code not found in PATH, open manually")

# ------------------------
# MAIN
# ------------------------

platform = input("Platform (leetcode/codeforces/hackerrank/gfg): ").lower()

number = ""
if platform == "leetcode":
    number = input("Problem number: ")
    title = input("Title: ")
    folder = f"{number}-{slugify(title)}"
    create_files("LeetCode", folder, folder, title, "LeetCode")

elif platform == "codeforces":
    title = input("Title: ")
    name = slugify(title)
    folder = f"codeforces-{name}"
    create_files("Codeforces", folder, folder, title, "Codeforces")

elif platform == "hackerrank":
    title = input("Title: ")
    name = slugify(title)
    folder = f"hacker-rank-{name}"
    create_files("HackerRank", folder, folder, title, "HackerRank")

elif platform in ["gfg", "geeksforgeeks"]:
    title = input("Title: ")
    name = slugify(title)
    folder = f"geeksforgeeks-{name}"
    create_files("GeeksforGeeks", folder, folder, title, "GeeksforGeeks")

else:
    print(" Unknown platform")
