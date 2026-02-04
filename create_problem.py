import os
import sys

# -------------------------
# Usage examples:
# python create_problem.py leetcode 1 "Two Sum"
# python create_problem.py codeforces "Watermelon"
# python create_problem.py hackerrank "Array Rotation"
# python create_problem.py gfg "Binary Search"
# -------------------------

def slugify(text):
    return text.lower().replace(" ", "-")

def create_files(base, folder_name, file_name, title, platform):
    path = os.path.join(base, folder_name)
    os.makedirs(path, exist_ok=True)

    # 1) solution file
    solution_file = os.path.join(path, f"{file_name}.py")
    with open(solution_file, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n# Platform: {platform}\n\n")

    # 2) README
    readme = os.path.join(path, "README.md")
    with open(readme, "w", encoding="utf-8") as f:
        f.write(f"""# {title}

## 🏷 Platform
{platform}

##  Problem Statement
(Add description here)

##  Approach
(Explain idea)

## ⏱ Complexity
Time:
Space:
""")

    # 3) NOTES (optional)
    notes = os.path.join(path, "NOTES.md")
    with open(notes, "w", encoding="utf-8") as f:
        f.write("# Notes\n\n")

    print(" Created:", path)


def main():
    if len(sys.argv) < 3:
        print("Usage: python create_problem.py <platform> <title/number> [title]")
        return

    platform = sys.argv[1].lower()

    if platform == "leetcode":
        number = sys.argv[2]
        title = sys.argv[3]
        name = slugify(title)

        folder = f"{number}-{title.replace(' ', '-')}"
        file_name = folder
        create_files("LeetCode", folder, file_name, title, "LeetCode")

    elif platform == "codeforces":
        title = sys.argv[2]
        name = slugify(title)

        folder = f"codeforces-{name}"
        create_files("Codeforces", folder, folder, title, "Codeforces")

    elif platform == "hackerrank":
        title = sys.argv[2]
        name = slugify(title)

        folder = f"hacker-rank-{name}"
        create_files("HackerRank", folder, folder, title, "HackerRank")

    elif platform in ["gfg", "geeksforgeeks"]:
        title = sys.argv[2]
        name = slugify(title)

        folder = f"geeksforgeeks-{name}"
        create_files("GeeksforGeeks", folder, folder, title, "GeeksforGeeks")

    else:
        print("Unknown platform")


if __name__ == "__main__":
    main()
