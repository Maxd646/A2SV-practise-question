import os
import subprocess

def slugify(text):
    return text.strip().lower().replace(" ", "-")

def multiline_input(prompt):
    print(prompt)
    print("(Finish by typing: END)")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def create_problem(platform, number, title):
    title_clean = title.replace(" ", "-")
    slug = slugify(title)

    if platform == "leetcode":
        base = "LeetCode"
        folder = f"{number}-{title_clean}"
        filename = folder
        platform_name = "LeetCode"

    elif platform == "codeforces":
        base = "Codeforces"
        folder = f"codeforces-{slug}"
        filename = folder
        platform_name = "Codeforces"

    elif platform == "hackerrank":
        base = "HackerRank"
        folder = f"hacker-rank-{slug}"
        filename = folder
        platform_name = "HackerRank"

    elif platform in ["gfg", "geeksforgeeks"]:
        base = "GeeksforGeeks"
        folder = f"geeksforgeeks-{slug}"
        filename = folder
        platform_name = "GeeksforGeeks"

    else:
        print("❌ Unknown platform")
        return

    path = os.path.join(base, folder)
    os.makedirs(path, exist_ok=True)

    # --- INPUTS ---
    solution_code = multiline_input("📌 Paste your SOLUTION CODE:")
    problem_desc = multiline_input("📌 Paste PROBLEM DESCRIPTION:")
    approach = multiline_input("📌 Paste APPROACH / LOGIC:")
    notes = multiline_input("📌 Paste NOTES (optional):")

    # --- WRITE FILES ---
    with open(os.path.join(path, f"{filename}.py"), "w", encoding="utf-8") as f:
        f.write(f"# {title}\n# Platform: {platform_name}\n\n")
        f.write(solution_code + "\n")

    with open(os.path.join(path, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"""# {title}

## 🏷 Platform
{platform_name}

## 🧠 Problem Statement
{problem_desc}

## 💡 Approach
{approach}

## ⏱ Complexity
- Time: 
- Space:
""")

    with open(os.path.join(path, "NOTES.md"), "w", encoding="utf-8") as f:
        f.write(notes if notes else "# Notes\n")

    print("✅ Problem created successfully!")

    # --- OPEN VS CODE ---
    try:
        subprocess.run(["code", path], check=True)
    except:
        print("⚠ VS Code not found in PATH")

# ---------------------------
# MAIN
# ---------------------------
platform = input("Platform (leetcode / codeforces / hackerrank / gfg): ").lower()

number = ""
if platform == "leetcode":
    number = input("LeetCode Problem Number: ")

title = input("Problem Title: ")

create_problem(platform, number, title)
