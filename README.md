# changelog-assistant

`changelog-assistant` генерирует release notes из Conventional Commits.

## Возможности v0.1

- чтение коммитов через `git log`
- группировка по типам: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `perf`, `other`
- вывод в `text` и `json`
- диапазон по ревизиям: `--since`, `--until`

## Использование

```bash
python3 -m pip install -e .
changelog-assistant generate --path . --since v0.1.0 --until HEAD
```

JSON-режим:

```bash
changelog-assistant generate --path . --format json
```
