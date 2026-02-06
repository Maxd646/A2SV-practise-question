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

n, m= map(int, input().split())
name=input().strip()
seen = 
for a in name:
    seen[a]=a
for _ in range(m):
    s, t= input().split()
    for ch in seen:
        if seen[ch]==s:
            seen[ch]=t
        elif seen[ch]==t:
            seen[ch]=s
answer= "".join(seen[ch] for ch in name)
print(answer)

"""

    # ---- README template ----
    readme_template = f"""# {title}

## Platform
{platform}

## Problem Statement

B. Rebranding
time limit per test2 seconds
memory limit per test256 megabytes
The name of one small but proud corporation consists of n lowercase English letters. The Corporation has decided to try rebranding — an active marketing strategy, that includes a set of measures to change either the brand (both for the company and the goods it produces) or its components: the name, the logo, the slogan. They decided to start with the name.

For this purpose the corporation has consecutively hired m designers. Once a company hires the i-th designer, he immediately contributes to the creation of a new corporation name as follows: he takes the newest version of the name and replaces all the letters xi by yi, and all the letters yi by xi. This results in the new version. It is possible that some of these letters do no occur in the string. It may also happen that xi coincides with yi. The version of the name received after the work of the last designer becomes the new name of the corporation.

Manager Arkady has recently got a job in this company, but is already soaked in the spirit of teamwork and is very worried about the success of the rebranding. Naturally, he can't wait to find out what is the new name the Corporation will receive.

Satisfy Arkady's curiosity and tell him the final version of the name.

Input
The first line of the input contains two integers n and m (1 ≤ n, m ≤ 200 000) — the length of the initial name and the number of designers hired, respectively.

The second line consists of n lowercase English letters and represents the original name of the corporation.

Next m lines contain the descriptions of the designers' actions: the i-th of them contains two space-separated lowercase English letters xi and yi.

Output
Print the new name of the corporation.

Examples
InputCopy
6 1
police
p m
OutputCopy
molice
InputCopy
11 6
abacabadaba
a b
b c
a d
e g
f a
b b
OutputCopy
cdcbcdcfcdc
Note
In the second sample the name of the corporation consecutively changes as follows:



## Approach
Hashing

## Complexity
Time:O(1)
Space:O(n+m)
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
