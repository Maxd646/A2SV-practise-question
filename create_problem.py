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
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        Max=0
        count=0
        for i in range(len(piles)):
            if i%2==1 and count<len(piles)//3:
                count+=1
                Max+=piles[i]
        return Max
"""

    # ---- README template ----
    readme_template = f"""# {title}

## Platform
{platform}

##  1561. Maximum Number of Coins You Can Get

There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.

 

Example 1:

Input: piles = [2,4,1,2,7,8]
Output: 9
Explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with 7 coins and Bob the last one.
Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with 2 coins and Bob the last one.
The maximum number of coins which you can have are: 7 + 2 = 9.
On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7) you only get 2 + 4 = 6 coins which is not optimal.
Example 2:

Input: piles = [2,4,5]
Output: 4
Example 3:

Input: piles = [9,8,7,6,5,1,2,3,4]
Output: 18
 

Constraints:

3 <= piles.length <= 105
piles.length % 3 == 0
1 <= piles[i] <= 104

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
