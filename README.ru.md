# changelog-assistant

[English version](README.md)

Генерация release notes из истории git и Conventional Commits.

## Возможности

- парсинг `git log`
- классификация коммитов по секциям (`feat`, `fix`, `docs`, `refactor`, `perf`, `test`, `chore`, `other`)
- поддержка диапазона ревизий (`--since`, `--until`)
- текстовый и JSON-вывод

## Использование

```bash
python3 main.py generate --path .
python3 main.py generate --path . --since v0.1.0 --until HEAD
python3 main.py generate --path . --format json
```
