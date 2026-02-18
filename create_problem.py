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

count= 0
n= int(input())
arra= list(map(int, input().split()))
arra.sort()
summ=0
for j in range(len(arra)):
    if arra[j]>summ:
        summ+=1
        count+=1
print(count)
"""

    # ---- README template ----
    readme_template = f"""# {title}

## Platform
{platform}

## B. Polycarp Training
    time limit per test   2 seconds
    memory limit per test   256 megabytes
    
Polycarp wants to train before another programming competition. During the first day of his training he should solve exactly 1
 problem, during the second day — exactly 2
 problems, during the third day — exactly 3
 problems, and so on. During the k
-th day he should solve k
 problems.

Polycarp has a list of n
 contests, the i
-th contest consists of ai
 problems. During each day Polycarp has to choose exactly one of the contests he didn't solve yet and solve it. He solves exactly k
 problems from this contest. Other problems are discarded from it. If there are no contests consisting of at least k
 problems that Polycarp didn't solve yet during the k
-th day, then Polycarp stops his training.

How many days Polycarp can train if he chooses the contests optimally?

Input
The first line of the input contains one integer n
 (1≤n≤2⋅105
) — the number of contests.

The second line of the input contains n
 integers a1,a2,…,an
 (1≤ai≤2⋅105
) — the number of problems in the i
-th contest.

Output
Print one integer — the maximum number of days Polycarp can train if he chooses the contests optimally.

Examples
InputCopy
4
3 1 4 1
OutputCopy
3
InputCopy
3
1 1 1
OutputCopy
1
InputCopy
5
1 1 1 2 2
OutputCopy
2



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
