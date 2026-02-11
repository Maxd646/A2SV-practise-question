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
    n, x, k = map(int, input().split())
    s = input().strip()
    
    pr = 0
    f = -1
    
    for i in range(n):
        if s[i] == 'L':
            pr -= 1
        else:
            pr += 1
        
        if pr== -x:
            f = i + 1
            break
    
    if f== -1 or f > k:
        print(0)
        continue
    
    an= 1
    r= k - f
    
    pr = 0
    cy= -1
    
    for i in range(n):
        if s[i] == 'L':
            pr-= 1
        else:
            pr += 1
        
        if pr == 0:
            cy = i + 1
            break
    
    if cy == -1:
        print(an)
    else:
        an += r // cy
        print(an)
"""

    # ---- README template ----
    readme_template = f"""# {title}

## Platform
{platform}

## B. Robot Program

There is a robot on the coordinate line. Initially, the robot is located at the point x
 (x≠0
). The robot has a sequence of commands of length n
 consisting of characters, where L represents a move to the left by one unit (from point p
 to point (p−1)
) and R represents a move to the right by one unit (from point p
 to point (p+1)
).

The robot starts executing this sequence of commands (one command per second, in the order they are presented). However, whenever the robot reaches the point 0
, the counter of executed commands is reset (i. e. it starts executing the entire sequence of commands from the very beginning). If the robot has completed all commands and is not at 0
, it stops.

Your task is to calculate how many times the robot will enter the point 0
 during the next k
 seconds.

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases.

The first line of a test case contains three integers n
, x
 and k
 (1≤n≤2⋅105
; −n≤x≤n
; n≤k≤1018
).

The second line of a test case contains a string s
 consisting of n
 characters L and/or R.

Additional constraint on the input: the sum of n
 over all test cases doesn't exceed 2⋅105
.

Output
For each test case, print a single integer — the number of times the robot will enter the point 0
 during the next k
 seconds.

Example
InputCopy
6
3 2 6
LLR
2 -1 8
RL
4 -2 5
LRRR
5 3 7
LRRLL
1 1 1
L
3 -1 4846549234412827
RLR
OutputCopy
1
4
1
0
1
2423274617206414
Note
In the first example, the robot moves as follows: 2→1→0–→−1→−2→−1
. The robot has completed all instructions from the sequence and is not at 0
. So it stops after 5
 seconds and the point 0
 is entered once.

In the second example, the robot moves as follows: −1→0–→1→0–→1→0–→1→0–→1
. The robot worked 8
 seconds and the point 0
 is entered 4
 times.

In the third example, the robot moves as follows: −2→−3→−2→−1→0–→−1
. The robot worked 5
 seconds and the point 0
 is entered once.

In the fourth example, the robot moves as follows: 3→2→3→4→3→2
. The robot has completed all instructions from the sequence and is not at 0
. So it stops after 5
 seconds, without reaching the point 0
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
