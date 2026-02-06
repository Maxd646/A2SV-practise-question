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
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)):
            result^=nums[i]
        return result
        
"""

    # ---- README template ----
    readme_template = f"""# {title}

## Platform
{platform}

## 136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

## Approach
Bit manupation -> for fastes one

## Complexity
Time:O(n)
Space:O(1)
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
