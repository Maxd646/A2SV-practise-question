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
    n, k=map(int, input().split())
    arra=[]
    for _ in range(n):
        aa=list(map(int, input().split()))
        arra.append(aa)
    arra.sort()
    for i in range(n):
        if arra[i][0]<=k<=arra[i][1]:
            k=max(arra[i][2], k)
    print(k)
"""

    # ---- README template ----
    readme_template = f"""# {title}

## Platform
{platform}

##  D. This Is the Last Time

   time      limit per test2 seconds
    memory     limit per test256 megabytes
    
You are given n
 casinos, numbered from 1
 to n
. Each casino is described by three integers: li
, ri
, and reali
 (li≤reali≤ri
). You initially have k
 coins.

You can play at casino i
 only if the current number of coins x
 satisfies li≤x≤ri
. After playing, your number of coins becomes reali
.

You can visit the casinos in any order and are not required to visit all of them. Each casino can be visited no more than once.

Your task is to find the maximum final number of coins you can obtain.

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains two integers n
 and k
 (1≤n≤105
, 0≤k≤109
) — the number of casinos and the initial number of coins.

This is followed by n
 lines. In the i
-th line, there are three integers li
, ri
, reali
 (0≤li≤reali≤ri≤109
) — the parameters of the i
-th casino.

It is guaranteed that the sum of all n
 across all test cases does not exceed 105
.

Output
For each test case, output a single integer — the maximum number of coins you can obtain after optimally choosing the order of visiting the casinos.

Example
InputCopy
5
3 1
2 3 3
1 2 2
3 10 10
1 0
1 2 2
1 2
1 2 2
2 2
1 3 2
2 4 4
2 5
1 10 5
3 6 5
OutputCopy
10
0
2
4
5
Note
In the first test case, you can first play at the 2
-nd casino. After that, you will have 2
 coins. Then you can play at the 1
-st casino, and the number of coins will increase to 3
. Finally, after playing at the 3
-rd casino, you will have 10
 coins — this is the maximum possible amount.

In the second test case, you have no money, so you cannot earn more.

In the fourth test case, it is beneficial to play at the 2
-nd casino right away and earn 4
 coins.
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
