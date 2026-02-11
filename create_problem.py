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

class Solution:
    def findValidPair(self, s: str) -> str:
        Count=Counter(s)
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                if Count[s[i]]==int(s[i]) and Count[s[i+1]]==int(s[i+1]):
                    return s[i:i+2]
        return ""
# or
class Solution:
    def findValidPair(self, s: str) -> str:
        Count=Counter(s)
        res=""
        seen= set()
        j=0
        for ch, num in Count.items():
            if int(ch)==num:
                res+=ch
        if len(res)<2:
            return ""
        seen= set(res)
        found=False
        for i in range(len(s)-1):
            if s[i] in seen and s[i+1] in seen:
                seen.add(s[i:i+2])
        
        found =False
        for i in range(len(s)):
            if s[i:i+2] in seen and len(set(s[i:i+2]))==2:
                found=True
                return s[i:i+2]
        if not found:
            return ""
"""

    # ---- README template ----
    readme_template = f"""# {title}

## Platform
{platform}

## 3438. Find Valid Pair of Adjacent Digits in String

You are given a string s consisting only of digits. A valid pair is defined as two adjacent digits in s such that:

The first digit is not equal to the second.
Each digit in the pair appears in s exactly as many times as its numeric value.
Return the first valid pair found in the string s when traversing from left to right. If no valid pair exists, return an empty string.

 

Example 1:

Input: s = "2523533"

Output: "23"

Explanation:

Digit '2' appears 2 times and digit '3' appears 3 times. Each digit in the pair "23" appears in s exactly as many times as its numeric value. Hence, the output is "23".

Example 2:

Input: s = "221"

Output: "21"

Explanation:

Digit '2' appears 2 times and digit '1' appears 1 time. Hence, the output is "21".

Example 3:

Input: s = "22"

Output: ""

Explanation:

There are no valid adjacent pairs.

 

Constraints:

2 <= s.length <= 100
s only consists of digits from '1' to '9'.

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
