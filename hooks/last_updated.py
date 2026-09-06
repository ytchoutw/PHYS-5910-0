"""Insert a 'Last updated' stamp under each page's H1, from git history.

Material's own last-update display lives in the page footer; this puts the date
at the top instead. The date is the last commit that touched the source file,
falling back to its modification time when git has no record of it (a new or
uncommitted file, or a build from a source archive).
"""

import os
import subprocess
from datetime import datetime

STAMP = '<p class="last-updated">Last updated: {date}</p>'


def _git_date(path):
    """Author date of the last commit touching *path*, or None."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%ad", "--date=short", "--", os.path.basename(path)],
            cwd=os.path.dirname(path),
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0 or not out.stdout.strip():
        return None
    try:
        return datetime.strptime(out.stdout.strip(), "%Y-%m-%d")
    except ValueError:
        return None


def on_page_markdown(markdown, page, config, files, **kwargs):
    path = page.file.abs_src_path
    if not path or not os.path.exists(path):
        return markdown

    when = _git_date(path) or datetime.fromtimestamp(os.path.getmtime(path))
    stamp = STAMP.format(date=when.strftime("%-d %B %Y"))

    lines = markdown.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("# "):
            lines.insert(i + 1, "\n" + stamp)
            return "\n".join(lines)

    return stamp + "\n\n" + markdown
