import subprocess
from pathlib import Path
from typing import Any, Optional


def _classify(message: str) -> str:
    lower = message.lower()
    for key in ("feat", "fix", "docs", "chore", "refactor", "test", "perf"):
        if lower.startswith(key + ":") or lower.startswith(key + "("):
            return key
    return "other"


def collect_commits(
    repo_path: Path, since: Optional[str] = None, until: str = "HEAD"
) -> list[dict[str, str]]:
    range_expr = until
    if since:
        range_expr = f"{since}..{until}"
    cmd = ["git", "-C", str(repo_path), "log", "--pretty=format:%H%x09%s", range_expr]
    out = subprocess.check_output(cmd, text=True)
    commits: list[dict[str, str]] = []
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, subject = line.split("\t", 1)
        commits.append({"sha": sha, "subject": subject, "type": _classify(subject)})
    return commits


def build_changelog(
    repo_path: Path, since: Optional[str] = None, until: str = "HEAD"
) -> dict[str, Any]:
    commits = collect_commits(repo_path, since=since, until=until)
    sections: dict[str, list[dict[str, str]]] = {
        k: []
        for k in ["feat", "fix", "docs", "refactor", "perf", "test", "chore", "other"]
    }
    for commit in commits:
        sections[commit["type"]].append(commit)
    return {
        "repo": str(repo_path),
        "since": since,
        "until": until,
        "total_commits": len(commits),
        "sections": sections,
    }


def render_text(report: dict[str, Any]) -> str:
    lines = [
        f"Repo: {report['repo']}",
        f"Range: {report['since'] or '(start)'}..{report['until']}",
        f"Total commits: {report['total_commits']}",
        "",
    ]
    for section, entries in report["sections"].items():
        if not entries:
            continue
        lines.append(f"## {section}")
        for commit in entries:
            lines.append(f"- {commit['subject']} ({commit['sha'][:7]})")
        lines.append("")
    return "\n".join(lines).rstrip()
