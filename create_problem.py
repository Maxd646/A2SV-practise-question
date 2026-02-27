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
from collections import Counter

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    colors = list(map(int, input().split()))

    left = Counter(colors[:l])
    right = Counter(colors[l:])


    for c in list(left.keys()):
        m = min(left[c], right[c])
        left[c] -= m
        right[c] -= m
        if left[c] == 0:
            del left[c]
        if right[c] == 0:
            del right[c]

    L = sum(left.values())
    R = sum(right.values())

    if L < R:
        left, right = right, left
        L, R = R, L

    cost = 0
    diff = L - R
    for c in left:
        while left[c] >= 2 and diff > 0:
            left[c] -= 2
            diff -= 2
            cost += 1


    cost += diff // 2

    remaining = sum(left.values()) + sum(right.values())
    cost += remaining // 2

    print(cost)
"""

    # ---- README template ----
    readme_template = f"""# {title}

## Platform
{platform}
##  D. Phoenix and Socks


## problem link:https://codeforces.com/contest/1515/problem/D
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
