import os

README_PATH = "README.md"
PROGRESS_START = "<!-- PROGRESS_START -->"
PROGRESS_END = "<!-- PROGRESS_END -->"

# Base directory where your difficulty folders are
BASE_DIR = '.'

DIFFICULTIES = ['Easy', 'Medium']

# Prepare lines for markdown content
lines = []
lines.append("## Progress Tracker\n")

for level in DIFFICULTIES:
    path = os.path.join(BASE_DIR, level)
    if not os.path.exists(path):
        continue

    problems = sorted([
        d for d in os.listdir(path)
        if d != '.DS_Store' and not d.startswith('.') and os.path.isdir(os.path.join(path, d))
        ])
    solved = 0

    total_probs = {
        "Easy": 41,
        "Medium": 115
    }
    total = total_probs.get(level, 0)

    # Build checklist for this difficulty
    entries = []
    for problem in problems:
        problem_path = os.path.join(path, problem)
        solution_file = os.path.join(problem_path, 'solution.py')
        is_solved = os.path.isfile(solution_file)
        if is_solved:
            solved += 1
        checkbox = '✅' if is_solved else ' '
        entries.append(f"- {checkbox} {problem} ({level})")

    lines.append(f"{level}: {solved} / {total} solved\n")
    lines.extend(entries)
    lines.append("")  # blank line for spacing

progress_content = "\n".join(lines)

# Read the original README
with open(README_PATH, "r") as f:
    readme_text = f.read()

# Replace the section between markers
if PROGRESS_START in readme_text and PROGRESS_END in readme_text:
    start_idx = readme_text.index(PROGRESS_START) + len(PROGRESS_START)
    end_idx = readme_text.index(PROGRESS_END)
    new_readme = (
        readme_text[:start_idx]
        + "\n\n"
        + progress_content
        + "\n\n"
        + readme_text[end_idx:]
    )

    # Write back to README.md
    with open(README_PATH, "w") as f:
        f.write(new_readme)

    print("✅ README.md updated with progress tracker.")
else:
    print("❌ Markers not found in README.md. Please add <!-- PROGRESS_START --> and <!-- PROGRESS_END --> in your README.md.")
