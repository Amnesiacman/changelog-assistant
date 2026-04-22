import argparse
import json
from pathlib import Path

from changelog_assistant.core import build_changelog, render_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="changelog-assistant",
        description="Generate release notes from git commits",
    )
    sub = parser.add_subparsers(dest="command")
    gen = sub.add_parser("generate", help="Generate changelog")
    gen.add_argument("--path", default=".")
    gen.add_argument("--since")
    gen.add_argument("--until", default="HEAD")
    gen.add_argument("--format", choices=("text", "json"), default="text")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.command != "generate":
        build_parser().print_help()
        return 1
    report = build_changelog(Path(args.path), since=args.since, until=args.until)
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=True))
    else:
        print(render_text(report))
    return 0
