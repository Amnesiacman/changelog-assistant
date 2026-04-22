# changelog-assistant

[Русская версия](README.ru.md)

Generate release notes from git history and Conventional Commits.

## Features

- parse `git log`
- classify commits into sections (`feat`, `fix`, `docs`, `refactor`, `perf`, `test`, `chore`, `other`)
- revision range support (`--since`, `--until`)
- text and JSON output

## Usage

```bash
python3 main.py generate --path .
python3 main.py generate --path . --since v0.1.0 --until HEAD
python3 main.py generate --path . --format json
```
