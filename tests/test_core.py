from changelog_assistant.core import _classify, render_text


def test_classify():
    assert _classify("feat: add api") == "feat"
    assert _classify("fix(parser): bug") == "fix"
    assert _classify("unknown change") == "other"


def test_render_text_minimal():
    report = {
        "repo": ".",
        "since": None,
        "until": "HEAD",
        "total_commits": 1,
        "sections": {
            "feat": [{"sha": "abcdef123", "subject": "feat: add x", "type": "feat"}],
            "fix": [],
            "docs": [],
            "refactor": [],
            "perf": [],
            "test": [],
            "chore": [],
            "other": [],
        },
    }
    text = render_text(report)
    assert "## feat" in text
    assert "feat: add x" in text
