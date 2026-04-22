import json

from changelog_assistant.cli import main


def test_help_path():
    assert main([]) == 1


def test_json_output_for_current_repo(capsys):
    code = main(["generate", "--path", ".", "--format", "json"])
    payload = json.loads(capsys.readouterr().out.strip())
    assert code == 0
    assert "total_commits" in payload
